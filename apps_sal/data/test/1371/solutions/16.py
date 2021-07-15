s = int(input())
MOD =10**9 +7

dp = [1]*(s+2)
dp[1] = 0
dp[2] = 0

if s < 6:
    print((dp[s]))
    return

for i in range(6,s+1):
    dp[i] = (dp[i-1] + dp[i-3])%MOD


print((dp[s]))

