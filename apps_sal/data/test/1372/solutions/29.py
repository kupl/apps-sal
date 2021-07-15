import numpy as np
h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
np_ab = np.array(ab)
max_a = max(np_ab[:, 0])
dp = [0]*(h+max_a)
for i in range(1, h+max_a):
    dp[i] = min(dp[i-a] + b for a,b in ab)
print(dp[h])
