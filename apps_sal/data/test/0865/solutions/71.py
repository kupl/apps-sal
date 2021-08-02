import numpy as np
import sys
input = sys.stdin.readline


n, t = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(n)]
dish.sort()

ans = 0
dp = np.zeros(t, dtype=int)
for time, point in dish:
    ans = max(ans, dp.max() + point)
    np.maximum(dp[time:], dp[:-time] + point, out=dp[time:])
print(ans)
