import numpy as np

n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 998244353

dp = np.array([[0] * 3 for _ in range(s + 1)], dtype=np.int64)
dp[0][0] = 1

for i, e in enumerate(a):
    cp = dp.copy()
    dp[:, 1] += cp[:, 0]
    dp[:, 2] += cp[:, 0] + cp[:, 1]

    dp[e:, 1] += cp[:-e, 0] + cp[:-e, 1]
    dp[e:, 2] += cp[:-e, 0] + cp[:-e, 1]

    dp %= mod

ans = dp[s][2]
print(ans)

