(N, K) = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort(key=lambda x: x[0])
ans = float('INF')
for i in range(N):
    for j in range(i + K - 1, N):
        W = XY[j][0] - XY[i][0]
        Y = [XY[x][1] for x in range(i, j + 1)]
        Y.sort()
        for (l, k) in zip(Y, Y[K - 1:]):
            H = k - l
            ans = min(ans, W * H)
print(ans)
