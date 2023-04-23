import string,random
#输入相应参数
pwd_length = int(input('请输入生成的密码长度：'))
pwd_uppercase = int(input('其中包含多少个大写字母，如没有则输入0：'))
pwd_digits = int(input('其中包含多少个数字，如没有则输入0：'))
pwd_punctuation = int(input('其中包含多少个特殊符号，如没有则输入0：'))
pwd_string = []

#生成密码
if pwd_length-pwd_uppercase-pwd_digits-pwd_punctuation < 0:
    print('特殊字符长度设置超出密码长度，请重新输入')
else:
    for a in random.choices(string.ascii_lowercase,k=pwd_length-pwd_uppercase-pwd_digits-pwd_punctuation):
        pwd_string += a
    for b in random.choices(string.digits,k=pwd_digits):
        pwd_string += b
    for c in random.choices(string.ascii_uppercase,k=pwd_uppercase):
        pwd_string += c
    for d in random.choices(string.punctuation,k=pwd_punctuation):
        pwd_string += d
        random.shuffle(pwd_string)
    #print(pwd_string)

#随机顺序并输出
realpass = ''
for d in pwd_string:
    realpass += d
print('您生成的密码结果为：{}'.format(realpass))
