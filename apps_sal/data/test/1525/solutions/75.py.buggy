import sys

h, w, k = map(int, input().split())
MOD = 1000000007

dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1

fn = [1, 1, 2, 3, 5, 8, 13, 21, 34]

if w == 1:
    print(1)
    return

for i in range(1, h + 1):
    for j in range(w):
        dp[i][j] = dp[i - 1][j] * fn[j] * fn[w - j - 1]
        if j < w - 1:
            dp[i][j] += dp[i - 1][j + 1] * fn[j] * fn[w - j - 2]
        if 0 < j:
            dp[i][j] += dp[i - 1][j - 1] * fn[j - 1] * fn[w - j - 1]
        dp[i][j] %= MOD

print(dp[-1][k - 1] % MOD)
