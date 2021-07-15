n, m = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]
x, xi, xj = 500, 0, 0
for i, gi in enumerate(g):
    for j, gij in enumerate(gi):
        if gij < x:
            x, xi, xj = gij, i, j
r, c = [g[i][xj] - x for i in range(n)], [g[xi][j] - x for j in range(m)]
for i, gi in enumerate(g):
    for j, gij in enumerate(gi):
        if gij != r[i] + c[j] + x:
            print(-1)
            return
print(min(n, m) * x + sum(r) + sum(c))
for i in range(n):
    for k in range(r[i] + (x if n <= m else 0)):
        print('row', i + 1)
for j in range(m):
    for k in range(c[j] + (x if m < n else 0)):
        print('col', j + 1)
