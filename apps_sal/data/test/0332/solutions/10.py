(n, m) = map(int, input().split())
m1 = []
m2 = []
for i in range(n):
    m1.append([int(j) for j in input().split()])
for i in range(n):
    m2.append([int(j) for j in input().split()])
d1 = [[] for i in range(n + m - 1)]
d2 = [[] for i in range(n + m - 1)]
for i in range(n):
    for j in range(m):
        d1[i + j].append(m1[i][j])
        d2[i + j].append(m2[i][j])
flag = True
for i in range(n + m - 1):
    d1[i].sort()
    d2[i].sort()
    if d1[i][:] != d2[i][:]:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
