n = input()
str = ''
for i in n:
    if i == '0' or i == '1':
        str = str + i
    if i == 'B':
        str = str[:-1]

print(str)
