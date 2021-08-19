L = input()
l = len(L)
dp = [[0] * 2 for _ in range(100002)]
# dp[i][smaller]: i桁目までみる　未満なら1
# dp[i][1] : i桁目までみて、a, bどちらもL未満
# dp[i][0] : i桁目までみて、a+b = L
dp[0][0] = 1
mod = 10**9 + 7

for i in range(l):
    n = L[i]

    if n == '1':
        dp[i + 1][0] += dp[i][0] * 2
        dp[i + 1][0] %= mod

        dp[i + 1][1] += dp[i][1] * 3 + dp[i][0]
        dp[i + 1][1] %= mod

    else:
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][0] %= mod

        dp[i + 1][1] += dp[i][1] * 3
        dp[i + 1][1] %= mod

print((dp[l][0] + dp[l][1]) % mod)
