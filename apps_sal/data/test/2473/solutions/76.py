(N, K) = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()
r = 10 ** 20
for xi0 in range(N - K + 1):
    for xi1 in range(K + xi0 - 1, N):
        x = XY[xi1][0] - XY[xi0][0]
        XY_ys = sorted(XY[xi0:xi1 + 1], key=lambda a: a[1])
        for yi0 in range(len(XY_ys) - K + 1):
            y = XY_ys[yi0 + K - 1][1] - XY_ys[yi0][1]
            r = min(r, x * y)
print(r)
