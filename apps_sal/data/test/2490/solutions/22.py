N=input()
inf=float("inf")
dp=[[inf]*(len(N)+1) for i in range(2)]
dp[0][0]=0
for i in range(len(N)):
   tmp=int(N[-1-i])
   dp[0][i+1]=min(dp[0][i],dp[1][i])+tmp
   dp[1][i+1]=min(dp[0][i]+11,dp[1][i]+9)-tmp
print(min(dp[0][-1],dp[1][-1]))
