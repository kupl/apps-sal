import numpy as np

n, s = map(int, input().split())
a = list(map(int, input().split()))

MOD = 998244353

dp = np.zeros(s + 1, dtype=int)  # 動的計画法を用いる
dp[0] = 1

for i in range(n):
    ddp = dp * 2 % MOD
    ddp[a[i]:] += dp[:-a[i]]  # 非常に大きな数になると考えられるため先にMOD計算を行う
    dp = ddp % MOD


print(dp[s])
