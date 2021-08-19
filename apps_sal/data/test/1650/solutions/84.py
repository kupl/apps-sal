import sys

sys.setrecursionlimit(10 ** 7)
# ----------

INF = float("inf")
MOD = 10 ** 9 + 7

s = input().strip()

dp = [[0] * 2 for _ in range(100005)]
dp[0][0] = 1

n = len(s)
for i in range(n):
    if s[i] == "0":
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD

    if s[i] == "0":
        dp[i + 1][1] += dp[i][1] * 2 % MOD
    else:
        dp[i + 1][0] += dp[i][0] * 2 % MOD
        dp[i + 1][1] += dp[i][1] * 2 % MOD

ans = (dp[n][0] + dp[n][1]) % MOD
print(ans)
