import numpy as np
n, t = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans = 0
dp = np.zeros(t, np.int64)
for i in range(n):
    a, b = ab[i]
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
print(ans)
