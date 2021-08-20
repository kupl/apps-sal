l = input()
n = len(l)
mod = 10 ** 9 + 7
dp = [[0, 0] for _ in range(n)]
dp[0] = [2, 1]
for i in range(1, n):
    if l[i] == '1':
        dp[i][0] = dp[i - 1][0] * 2
        dp[i][1] = dp[i - 1][1] * 3 + dp[i - 1][0]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] * 3
    dp[i][0] %= mod
    dp[i][1] %= mod
print(sum(dp[n - 1]) % mod)
