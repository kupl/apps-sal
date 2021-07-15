read = lambda: list(map(int, input().split()))
r, c, n, k = read()
a = [[0] * (c + 1) for i in range(r + 1)]
for i in range(n):
    x, y = read()
    a[x][y] = 1
d = [[0] * (c + 1) for i in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if a[i][j]: d[i][j] += 1
        if i == j == 0: continue
        p1 = d[i - 1][j] if i else 0
        p2 = d[i][j - 1] if j else 0
        p3 = d[i - 1][j - 1] if i and j else 0
        d[i][j] += p1 + p2 - p3
cnt = 0
for x1 in range(r + 1):
    for y1 in range(c + 1):
        for x2 in range(x1 + 1, r + 1):
            for y2 in range(y1 + 1, c + 1):
                cur = d[x2][y2] - d[x2][y1] - d[x1][y2] + d[x1][y1]
                if cur >= k: cnt += 1
print(cnt)

