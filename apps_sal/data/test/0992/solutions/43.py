import numpy as np

n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 998244353

dp = np.zeros(s + 1, np.int64)
dp[0] = 1

for e in a:
    pre = dp.copy()
    dp = pre * 2
    dp[e:] += pre[:-e]
    dp %= mod

ans = dp[s]
print(ans)

