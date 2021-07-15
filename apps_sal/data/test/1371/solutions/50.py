s = int(input())
dp = [0] * (max(s+1,6))
dp[3],dp[4],dp[5] = 1,1,1
x = 1
for i in range(6,s+1):
    dp[i] = (x+1) % (10**9+7)
    x += dp[i-2]
print(dp[s])
