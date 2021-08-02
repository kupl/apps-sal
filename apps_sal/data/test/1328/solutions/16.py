import numpy as np
N, Ma, Mb = map(int, input().split())
ls = []
dp = np.full((1001, 1001), float('inf'))
dp[0][0] = 0
for i in range(N):
    a, b, c = map(int, input().split())
    dp[a:, b:] = np.minimum(dp[:1001 - a, :1001 - b] + c, dp[a:, b:])
ans = float('inf')
for i in range(1, 1001):
    if i * Ma > 1000 or i * Mb > 1000:
        break
    if dp[i * Ma, i * Mb] < ans:
        ans = dp[i * Ma, i * Mb]
if ans == float('inf'):
    ans = -1
print(int(ans))
