l = list(input())
for i in range(len(l)):
    if l[i] == '1':
        l[i] = '9'
    elif l[i] == '9':
        l[i] = '1'
print((''.join(l)))
