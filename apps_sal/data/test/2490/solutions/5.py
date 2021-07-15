n=input()
k=len(n)
dp=[[0]*2 for _ in range(k)]
dp[0][0]=min(int(n[0]),11-int(n[0]))
dp[0][1]=min(int(n[0])+1,11-(int(n[0])+1))
for i in range(1,k):
  dig=int(n[i])
  dp[i][0]=min(dp[i-1][0]+dig,dp[i-1][1]+10-dig)
  dp[i][1]=min(dp[i-1][0]+dig+1,dp[i-1][1]+10-(dig+1))
print(dp[k-1][0])
