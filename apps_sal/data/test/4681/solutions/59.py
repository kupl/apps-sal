n = int(input())
import sys
dp = [0]*(n+3)

dp[0]=2
dp[1]=1
if n<=1:
    print(dp[n])
    return

for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])
