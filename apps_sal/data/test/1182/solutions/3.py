(r, c, n, k) = map(int, input().split())
(g, v) = ([[False] * c for i in range(r)], 0)
for i in range(n):
    (x, y) = map(int, input().split())
    g[x - 1][y - 1] = True
for a in range(r):
    for b in range(c):
        for e in range(a, r):
            for f in range(b, c):
                x = sum((g[i][j] for i in range(a, e + 1) for j in range(b, f + 1)))
                if x >= k:
                    v += 1
print(v)
