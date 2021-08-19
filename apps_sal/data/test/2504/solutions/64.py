from scipy.sparse.csgraph import floyd_warshall

n, m, l = map(int, input().split())
inf = 10**12
d = [[inf for i in range(n)] for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x, y, z = map(int, input().split())
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０
dd = floyd_warshall(d)
ddd = [[inf for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if dd[i][j] <= l:
            ddd[i][j] = 1
dddd = floyd_warshall(ddd)
q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    if dddd[s - 1][t - 1] == inf:
        print(-1)
    else:
        print(int(dddd[s - 1][t - 1] - 1))
