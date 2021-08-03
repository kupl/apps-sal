n = int(input())
ip = []
op = []
b = 0
for i in range(n):
    s = str(input().split())
    ip.append(s)
    if 'OO' in s and b == 0:
        j = s.index('OO')
        s = s[:j] + '++' + s[j + 2:]
        b = 1
    op.append(s)
if b == 0:
    print('NO')
else:
    print('YES')
    for i in op:
        print(i[2:7])
