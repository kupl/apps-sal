n = int(input())
mod = 10**9+7

dp = [0] * n
dp[0] = 1
tot = 1
for i in range(1,n):
    if(i==1):
        dp[i] = tot
    else:
        dp[i] = tot - dp[i-2]
    dp[i] %= mod
    tot += dp[i]
    tot %= mod

ans = 0
for i in range(n-1):
    ans += dp[i] * ((n-1)**2 + min(n-1, i+2))
    ans %= mod

ans += dp[-1]*n
ans %= mod
print(ans)
