f = lambda: map(int, input().split())
g = lambda k: k * k - k >> 1
n, k = f()
p = list(f())

a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if p[i] > p[j]: a[i][j] = 1
        else: a[j][i] = 1

for t in range(k):
    b = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            p = q = 0

            for x in range(j):
                d = min(i + 1, j - x, x + 1, j - i)
                p += d * a[x][j]
                q += d

            for y in range(i + 1, n):
                d = min(n - j, y - i, n - y, j - i)
                p += d * a[i][y]
                q += d

            for s in range(j, i + n):
                x, y = s - i, s - j
                d = min(i + 1, n - j, y + 1, n - x)
                p += d * a[x][y]
                q += d

            d = g(j - i) + g(i + 1) + g(n - j)
            b[i][j] = (p + d * a[i][j]) / (d + q)
    a = b
    for i in range(n):
        for j in range(i + 1, n):
            a[j][i] = 1 - a[i][j]

s = 0
for i in range(n):
    for j in range(i + 1, n): s += a[i][j]
print(s)
