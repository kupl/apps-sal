n = input()
m = ''
for x in n:
    if x == '1':
        m += '9'
    elif x == '9':
        m += '1'
    else:
        m += x
print(int(m))
