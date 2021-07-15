n = int(input())
pt = [0] + list(map(int, input().split(" ")))
dp = [0 for i in range(1005)]
MOD = int(1e9+7)
for i in range(1, n+1):
    dp[i+1] = (2*dp[i] + 2 - dp[pt[i]])%MOD
print(dp[n+1]%MOD)

