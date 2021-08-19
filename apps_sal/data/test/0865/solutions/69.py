import numpy as np
(N, T) = map(int, input().split())
AB = []
for i in range(N):
    (A, B) = map(int, input().split())
    AB.append([A, B])
AB.sort()
dp = np.zeros(T, dtype=int)
ans = 0
for (a, b) in AB:
    ans = max(ans, dp[-1] + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
print(ans)
