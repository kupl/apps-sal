import numpy as np

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB)

dp = np.zeros(T, np.int64)
ans = 0
for a, b in AB:
    ans = max(ans, dp.max() + b)
    np.maximum(dp[a:], dp[:-a] + b, out=dp[a:])
print(ans)
