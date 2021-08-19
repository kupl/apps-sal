import numpy as np
(N, T) = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))
AB.sort(key=lambda x: (x[0], -x[-1]))
dp = np.array([0] * T)
ans = 0
for (a, b) in AB:
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[:-a] + b, dp[a:])
print(max(ans, dp[-1]))
