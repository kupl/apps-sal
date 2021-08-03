import sys
import numpy as np
input = sys.stdin.readline

n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: (x[0], -x[1]))

dp = np.array([0] * t)
ans = 0

for a, b in ab:
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[:-a] + b, dp[a:])
print(max(ans, dp[-1]))
