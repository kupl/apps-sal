s = str(input())
n = len(s)
x = [''] * n
for i in range(n):
    x[i] = s[i]
for i in range(n):
    if int(s[i]) * 2 > 9:
        if i == 0 and s[i] == '9':
            x[i] = '9'
        else:
            x[i] = str(9 - int(s[i]))
print(''.join(x))
