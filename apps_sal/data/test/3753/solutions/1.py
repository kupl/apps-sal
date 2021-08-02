import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if n == 1:
    f = input().strip()
    if '#' in f:
        print(0)
    else:
        print(1)
    return
if m == 1:

    f = input().strip()
    for i in range(n):
        if '#' == f:
            print(0)
            break
        f = input().strip()
    else:
        print(1)
    return

a = []
for i in range(n):
    b = input().strip()
    d = []
    for j in range(m):
        if b[j] == '.':
            d.append(1)
        else:
            d.append(0)
    a.append(d)
gr = [[] for i in range(n * m + 5)]
for i in range(2, n + 1):
    for j in range(2, m + 1):
        if a[i - 2][j - 1] == 1:
            gr[(i - 1) * m + j].append((i - 2) * m + j)
        if a[i - 1][j - 2] == 1:
            gr[(i - 1) * m + j].append((i - 1) * m + j - 1)


for i in range(2, n + 1):
    if a[i - 2][0] == 1:
        gr[(i - 1) * m + 1].append((i - 2) * m + 1)
for j in range(2, m + 1):
    if a[0][j - 2] == 1:
        gr[j].append(j - 1)
if a[n - 1][m - 2] == 1:
    gr[n * m].append(n * m - 1)
if a[n - 2][m - 1] == 1:
    gr[n * m].append(n * m - m)

v = [False for i in range(n * m + 6)]
if a[n - 1][m - 2] == 1:
    s = [n * m - 1]
    t = True
    while s and t:
        x = s.pop()
        if x == 1:
            t = False
        v[x] = True
        for j in gr[x]:
            if v[j]:
                continue
            s.append(j)
ans = 0
if v[1]:
    ans += 1
v[1] = False
if a[n - 2][m - 1] == 1:
    s = [n * m - m]
    while s:
        x = s.pop()
        v[x] = True
        for j in gr[x]:
            if v[j]:
                continue
            s.append(j)
if v[1]:
    ans += 1
print(ans)
