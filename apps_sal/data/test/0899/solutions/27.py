# ワーシャルフロイド法
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


##############################
n, m = map(int, input().split())

d = [[float("inf")] * n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
edge = []
for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    edge.append((x, y, c))
    d[x][y] = c
    d[y][x] = c
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０
d = warshall_floyd(d)
ans = 0
for x, y, c in edge:
    if d[x][y] < c:
        ans += 1
print(ans)
