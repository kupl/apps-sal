n = input()
a = ''
for i in range(len(n)):
    if n[i] == '1':
        a += '9'
    elif n[i] == '9':
        a += '1'
print(a)
