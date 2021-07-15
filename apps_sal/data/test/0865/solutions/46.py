import numpy as np

n, t = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort()

dp = np.zeros(t, dtype=np.int64)

ans = 0
for a, b in ab:
    ans = max(ans, dp[-1] + b)
    np.maximum(dp[a:], dp[:-a] + b, out=dp[a:])


print(ans)

