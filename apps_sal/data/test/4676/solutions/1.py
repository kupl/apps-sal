o = input()
e = input()
password = ''
for i in range(len(o)):
    password += o[i]
    if len(e) > i:
        password += e[i]
print(password)
