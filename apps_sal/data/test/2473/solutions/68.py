N, K = list(map(int, input().split()))
XY = []
X = []
Y = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    XY.append((x, y))
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
ix = {v: i for i, v in enumerate(X)}
iy = {v: i for i, v in enumerate(Y)}
m = [[0] * (len(X) + 1) for _ in range(len(Y) + 1)]
for x, y in XY:
    m[iy[y] + 1][ix[x] + 1] += 1
for y in range(len(Y) + 1):
    for x in range(len(X)):
        m[y][x + 1] += m[y][x]
for x in range(len(X) + 1):
    for y in range(len(Y)):
        m[y + 1][x] += m[y][x]
ans = float("inf")
for x0 in range(len(X) - 1):
    for x1 in range(x0 + 1, len(X)):
        for y0 in range(len(Y) - 1):
            for y1 in range(y0 + 1, len(Y)):
                n = m[y1 + 1][x1 + 1] - m[y0][x1 + 1] - \
                    m[y1 + 1][x0] + m[y0][x0]
                if n >= K:
                    s = (X[x1] - X[x0]) * (Y[y1] - Y[y0])
                    ans = min(ans, s)
print(ans)

