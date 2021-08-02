N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()
X, Y = zip(*XY)
r = 10**20
for x0 in range(N - K + 1):
    for x1 in range(K + x0 - 1, N):
        Ys = sorted(Y[x0:x1 + 1])
        for y0 in range(len(Ys) - K + 1):
            r = min(r, (X[x1] - X[x0]) * (Ys[y0 + K - 1] - Ys[y0]))
print(r)
