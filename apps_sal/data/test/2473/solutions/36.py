"""
座標圧縮
2D累積和
全探索
勝利
"""
n, k = map(int, input().split())
xs = set()
ys = set()
ps = []
for _ in range(n):
    x, y = map(int, input().split())
    ps.append((x, y))
    xs.add(x)
    ys.add(y)
xdic = {x: i for i, x in enumerate(sorted(list(xs)))}
ydic = {y: i for i, y in enumerate(sorted(list(ys)))}
rxdic = {i: x for i, x in enumerate(sorted(list(xs)))}
rydic = {i: y for i, y in enumerate(sorted(list(ys)))}

h = len(xdic)
w = len(ydic)
A = [[0 for i in range(w + 1)] for j in range(h + 1)]
Acum = [[0 for i in range(w + 1)] for j in range(h + 1)]

for x, y in ps:
    h = xdic[x]
    w = ydic[y]
    A[h][w] += 1

for i in range(len(xdic)):
    for j in range(len(ydic)):
        Acum[i + 1][j + 1] = Acum[i][j + 1] + Acum[i + 1][j] - Acum[i][j] + A[i][j]

ans = 1 << 100
h = len(xdic)
w = len(ydic)
for i1 in range(h + 1):
    for i2 in range(i1 + 1, h + 1):
        for j1 in range(w + 1):
            for j2 in range(j1 + 1, w + 1):
                num = Acum[i2][j2] - Acum[i1][j2] - Acum[i2][j1] + Acum[i1][j1]
                if num == k:
                    x1 = rxdic[i1]
                    x2 = rxdic[i2 - 1]
                    y1 = rydic[j1]
                    y2 = rydic[j2 - 1]
                    S = (x2 - x1) * (y2 - y1)
                    ans = min(ans, S)
print(ans)
