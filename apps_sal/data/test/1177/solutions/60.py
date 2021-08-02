import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 998244353
N, S = lr()
A = lr()
dp = np.array([0] * (S + 1), dtype=np.int64)
answer = 0
for a in A:
    dp[0] += 1  # Lの数は１個ずつ加わる
    prev = dp.copy()
    dp[a:] += prev[:-a]
    answer += dp[-1]  # その位置をRとした時
    dp %= MOD

print((answer % MOD))
# 26
