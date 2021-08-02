N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()
X, Y = zip(*XY)
r = 10**20
for x0 in range(N - K + 1):
    for x1 in range(K + x0 - 1, N):
        x = X[x1] - X[x0]
        Y_s = sorted(Y[x0:x1 + 1])
        for y0 in range(len(Y_s) - K + 1):
            y = Y_s[y0 + K - 1] - Y_s[y0]
            r = min(r, x * y)
print(r)
