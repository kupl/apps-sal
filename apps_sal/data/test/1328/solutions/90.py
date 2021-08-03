N, Ma, Mb = map(int, input().split())

kusuri = []
cusum = [0] * (N + 1)
for i in range(N):
    a, b, c = map(int, input().split())
    sa = a * Mb - b * Ma
    kusuri.append((sa, c))
    cusum[i + 1] = cusum[i] + c

call = cusum[-1]
dp = [[call + 1] * 8001 for _ in range(41)]
dp[0][4000] = 0

cmin = call + 1
for i, j in enumerate(kusuri):
    d = j[0]
    c = j[1]
    for k in range(4000 - 100 * i, 4000 + 100 * i + 1):
        dp[i + 1][k] = min(dp[i + 1][k], dp[i][k])
        if k + d == 4000:
            cmin = min(cmin, dp[i][k] + c)
        dp[i + 1][k + d] = min(dp[i + 1][k + d], dp[i][k] + c)


if cmin == call + 1:
    print(-1)
else:
    print(cmin)
