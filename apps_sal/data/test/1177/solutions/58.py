import numpy as np

n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [np.zeros(s + 1, dtype=np.int64) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
ans = 0

for i, w in enumerate(a):
    dp[i] += dp[i - 1]
    dp[i][w:] += dp[i - 1][:-w]
    dp[i] %= 998244353
    ans += dp[i][-1]
    ans %= 998244353

print(ans)
