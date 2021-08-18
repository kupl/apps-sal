import sys
n, m = list(map(int, input().split()))
l = ['-'] * n
for i in range(m):
    s, c = list(map(int, input().split()))
    c = str(c)
    if l[s - 1] != c and l[s - 1] != '-':
        print('-1')
        return
    else:
        l[s - 1] = c

if n == 1 and l[0] == '0':
    print('0')
    return
if n == 1 and l[0] == '-':
    print('0')
    return
if l[0] == '0':
    print('-1')
    return

if l[0] == '-':
    l[0] = '1'

for j in range(n):
    if l[j] == '-':
        l[j] = '0'

print((''.join(l)))
