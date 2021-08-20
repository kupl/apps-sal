(n, m) = list(map(int, input().split()))
a = [0 for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
f = [0 for i in range(m)]
g = [[0 for i in range(m)] for j in range(m)]
ans = s = p = q = 0
c = n
for i in range(m):
    for j in range(b[i][0] - 1, b[i][1]):
        a[j] += 1
for i in range(n):
    s += a[i] != 0
    if a[i] == 1:
        for j in range(m):
            if b[j][0] - 1 <= i < b[j][1]:
                f[j] += 1
    if a[i] == 2:
        p = q = -1
        for j in range(m):
            if b[j][0] - 1 <= i < b[j][1]:
                if p == -1:
                    p = j
                else:
                    q = j
        g[p][q] += 1
for i in range(m):
    for j in range(i + 1, m):
        c = min(c, g[i][j] + f[i] + f[j])
print(s - c)
