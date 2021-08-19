(N, K, *XY) = map(int, open(0).read().split())
(X, Y) = zip(*sorted(zip(*[iter(XY)] * 2)))
ans = 1e+20
for k in range(K, N + 1):
    for i in range(N - k + 1):
        dx = X[i + k - 1] - X[i]
        YY = sorted(Y[i:i + k])
        ans = min(ans, min((dx * (YY[j + K - 1] - YY[j]) for j in range(k - K + 1))))
print(ans)
