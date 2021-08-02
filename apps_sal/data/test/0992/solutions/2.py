import numpy as np
n, s = map(int, input().split())
a = list(map(int, input().split()))
dp = np.zeros(s + 1, dtype=np.int64)
"""
dp[i][j] := i番目までを選んで、和がちょうどjのときの場合の数
遷移 → 1増えると全体集合に選ぶ, Aには選ばない, Aに選ぶの3種類.
"""
mod = 998244353
dp[0] = 1
for i in range(n):
    p = (dp * 2) % mod
    p[a[i]:] += dp[:-a[i]]
    dp = p % mod
print(dp[s])
