n, m = map(int, input().split())

l = []
for i in range(m):
    a, b, c = map(int, input().split())
    l.append((c, a, b))
l.sort()
f = [i for i in range(n + 1)]
c = [1] * (n + 1)


def r(a):
    if a != f[a]:
        f[a] = r(f[a])
    return f[a]


def union(x, y):
    if x == y:
        return
    if c[x] < c[y]:
        f[x] = y
    else:
        if c[x] == c[y]:
            c[x] = c[x] + 1
        f[y] = x


cnt = 0
i = 0
while i < m:
    j = i
    while j < m and l[j][0] == l[i][0]:
        j = j + 1
    num = 0
    for k in range(i, j):
        x = r(l[k][1])
        y = r(l[k][2])
        if x != y:
            num = num + 1
    for k in range(i, j):
        x = r(l[k][1])
        y = r(l[k][2])
        if x != y:
            union(x, y)
            num = num - 1
    cnt = cnt + num
    i = j
print(cnt)
