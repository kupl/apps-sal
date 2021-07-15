INF = float("inf")

N, K, *XY = map(int, open(0).read().split())

X, Y = zip(*sorted(zip(*[iter(XY)] * 2)))

ans = INF
for k in range(K, N + 1):
    for i in range(N - k + 1):
        dx = X[i + k - 1] - X[i]
        YY = sorted(Y[i:i + k])
        for j in range(k - K + 1):
            dy = YY[j + K - 1] - YY[j]
            if ans > dx * dy:
                ans = dx * dy

print(ans)
