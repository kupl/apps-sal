s = [int(x) for x in input().split()]
c = []
a = [False for x in range(s[0])]
for _ in range(s[0]):
    c.append(input())
for i in range(s[1]):
    last = -1
    q = 0
    for j in range(s[0]):
        if c[j][i] == '1':
            last = j
            q += 1
    if q == 1:
        a[last] = True
if all((x for x in a)):
    print('NO')
else:
    print('YES')
