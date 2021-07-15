MOD = 10 ** 9 + 7

n = int(input())

if n == 1:
    print(1)
    return

dp = [0] * (n)
dp[0] = 1
dp[1] = 1
dpsum = 2
for l in range(2, n):
    dp[l] = dpsum
    dp[l] -= dp[l-2]
    dp[l] %= MOD
    dpsum += dp[l]
    dpsum %= MOD

ans = 1 + (dpsum - dp[-1]) * (n-1) # end with "1..."
ans %= MOD
for l in range(n-1):
    ans += dp[l] * (n - 1) ** 2
    ans %= MOD

ans += dp[n-1] * (n - 1)
ans %= MOD

print(ans)
