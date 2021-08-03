n, k = list(map(int, input().split()))
ps = [tuple(map(int, input().split())) for i in range(n)]

sx = sorted(ps, key=lambda x: x[0])  # x座標でソート
nx = list(enumerate(sx))  # 頂点番号を付加
ans = 5e18

for f, (x1, y1) in nx[:n - k + 1]:  # 左辺の頂点
    for e, (x2, y2) in nx[f + k - 1:]:  # 右辺の頂点
        dx = x2 - x1  # 横
        sy = sorted(y for x, y in sx[f:e + 1])  # 含まれる頂点をy座標でソート
        for y3, y4 in zip(sy, sy[k - 1:]):  # y3=下辺の頂点，y4=上辺の頂点
            if y3 <= y1 and y4 >= y2:  # 左右辺の頂点を含むこと
                ans = min(ans, dx * (y4 - y3))

print(ans)
