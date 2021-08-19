MOD = 998244353
fac = [1] * 1000007
for i in range(2, 1000001):
    fac[i] = fac[i - 1] * i
    fac[i] %= MOD
dp = [0] * 1000007
for i in range(3, 1000001):
    dp[i] = (dp[i - 1] + fac[i - 1] - 1) * i
    dp[i] %= MOD
# print(dp[1:11])

n = int(input())

ans = (fac[n] + dp[n]) % MOD
print(ans)
