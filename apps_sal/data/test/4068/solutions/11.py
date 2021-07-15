import numpy as np

mod = 1000000007
N, M = map(int, input().split())
a = np.array([int(input()) for _ in range(M)])

dp = np.full(N+1, -1)
dp[0] = 1
index = 0 # aを順に走査するためのインデックス
for i in range(1, N+1):
    if index < M and i == a[index]: # 壊れている場合
        dp[i] = 0
        index += 1
    else: # 壊れていない場合
        dp[i] = dp[i-1]
        if i >= 2:
            dp[i] += dp[i-2]
        dp[i] %= mod

print(dp[N])
