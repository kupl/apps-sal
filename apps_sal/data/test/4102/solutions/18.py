n = str(input())
s = ''
for i in range(len(n)):
    if n[i] == '1' or n[i] == '2':
        s = s + '.'
    elif n[i] == '3' or n[i] == '7':
        s = s + n[i]
    elif n[i] == '4':
        s = s + '6'
    elif n[i] == '6':
        s = s + '4'
    elif n[i] == '5':
        s = s + '9'
    elif n[i] == '9':
        s = s + '5'
    elif n[i] == '0':
        s = s + '8'
    elif n[i] == '8':
        s = s + '0'
k = ''
for i in range(len(n) - 1, -1, -1):
    k = k + s[i]
if k != n:
    print('No')
else:
    print('Yes')
