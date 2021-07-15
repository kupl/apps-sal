import sys
a = input()
n = int(input())
s = ''
for i in a:
    if (i == 'O') or (i == 'o'):
        s = s + '0'
    else:
        if (i == 'l') or (i == 'I') or (i == 'L') or (i == 'i'):
            s = s + '1'
        else:
            s = s + i.lower()
for j in range(n):
    a = input()
    str = ''
    for i in a:
        if (i == 'O') or (i == 'o'):
            str = str + '0'
        else:
            if (i == 'l') or (i == 'I') or (i == 'L') or (i == 'i'):
                str = str + '1'
            else:
                str = str + i.lower()
    if s == str:
        print('No')
        return
print('Yes')

