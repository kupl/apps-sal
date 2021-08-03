# ワーシャルフロイド法 O(Nの3乗)。N <= 300くらいで解ける。
a, b, x, y = map(int, input().split())
g = [[10**8 for _ in range(200)] for i in range(200)]
# g[i][j]=aのi階からbのj階までの最短時間
for i in range(200):
    g[i][i] = 0
# A_iを0-indexの(0 ～99 ) B_iを0-indexの(100～199)で考える
for i in range(100):
    g[i][i + 100] = x
    g[i + 100][i] = x
for i in range(99):
    g[i + 1][i + 100] = x
    g[i + 100][i + 1] = x
for i in range(99):
    g[i + 1][i] = y
    g[i][i + 1] = y
for i in range(99):
    g[i + 101][i + 100] = y
    g[i + 100][i + 101] = y
# ワーシャルフロイド法


def warchall_floyd(n):
    for i in range(n):
        # 経由する頂点
        for j in range(n):
          # 始点
            for k in range(n):
                # 終点
                g[j][k] = min(g[j][k], g[j][i] + g[i][k])


warchall_floyd(200)
print(g[a - 1][100 + b - 1])
