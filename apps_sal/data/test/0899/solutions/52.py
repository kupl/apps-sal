n, m = map(int, input().split())
INF = float("inf")
g = [[INF] * n for _ in range(n)]
e = []
for i in range(m):
    vi, vj, w = map(int, input().split())
    g[vi - 1][vj - 1] = w
    g[vj - 1][vi - 1] = w
    e.append((vi - 1, vj - 1, w))

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])
cnt = 0
for x, y, z in e:
    if g[x][y] < z:
        cnt += 1
print(cnt)
