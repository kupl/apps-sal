import numpy as np

N, M = list(map(int, input().split()))
S = list(map(int, input().split()))
T = np.array(list(map(int, input().split())))

dp = np.ones(M + 1, dtype='int64')

for s in S:
    dp[1:] = ((dp[:-1] * (s == T)).cumsum() + dp[1:]) % (10**9 + 7)
print(dp[-1])
