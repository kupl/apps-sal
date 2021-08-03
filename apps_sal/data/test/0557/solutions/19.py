n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
m1 = 0
for i in range(n):
    if a[i][0] <= m1 and a[i][1] >= m1:
        m1 = a[i][1]

if m1 >= m:
    print('YES')
else:
    print('NO')
