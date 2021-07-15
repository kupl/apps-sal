import numpy as np

n, t = map(int, input().split())
dt = [list(map(int, input().split())) for _ in range(n)]
dt.sort()
dp = np.zeros(t, dtype=int)
ans = 0
for a, b in dt:
    ans = max(ans, dp[-1]+b)
    np.maximum(dp[a:], dp[:-a]+b, out=dp[a:])
print(ans)
