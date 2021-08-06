n = int(input())
dp = [0 for i in range(n + 1)]
dp[0] = 1
x = (n - 1)**2
dp[1] = n
pref = dp[1]
mod = 10**9 + 7
x %= mod
for i in range(2, n + 1):
    dp[i] += x + pref - dp[i - 2] + (n - i + 2)
    pref += dp[i]
    pref %= mod
    dp[i] %= mod

print((dp[-1]))
