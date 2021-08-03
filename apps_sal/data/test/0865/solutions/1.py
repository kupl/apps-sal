import numpy as np
n, t = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l.sort()
dp = np.array([0] * t)
ans = 0
for a, b in l:
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)


print(max(ans, dp[-1]))
