import numpy as np
n, ma, mb = map(int, input().split())
r = 10 * n + 6
inf = 10**5
dp = np.full((n+1, r, r), inf)
dp[0][0][0] = 0
for i in range(n):
    a, b, c = map(int, input().split())
    dp[i+1][a:, b:] = np.minimum(
        dp[i][:r-a, :r-b] + c, dp[i][a:, b:]
    )
    dp[i+1] = np.minimum(dp[i+1], dp[i])

ans = inf
x, y = 0, 0
while True:
    x += ma
    y += mb
    if x < r and y < r:
        ans = min(ans, dp[n][x][y])
    else:
        break
if ans == inf:
    print(-1)
else:
    print(int(ans))
