def cum2D(a, H, W):
    cum = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            cum[i + 1][j + 1] = cum[i][j + 1] + cum[i + 1][j] - cum[i][j] + a[i + 1][j + 1]
    return cum


n, m, q = list(map(int, input().split()))
trains = [tuple(map(int, input().split())) for _ in range(m)]
a = [[0] * (n + 1) for j in range(n + 1)]
for k in range(m):
    start, stop = trains[k]
    a[start][stop] += 1
cum = cum2D(a, n, n)

for _ in range(q):
    p, q = list(map(int, input().split()))
    print((cum[n][q] - cum[p - 1][q]))
