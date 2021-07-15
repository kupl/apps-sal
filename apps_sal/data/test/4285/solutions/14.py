l=int(input())
s=input()
mod=10**9+7
dp=[[0,0,0,0] for _ in range(l+1)]
for i in range(l,-1,-1):
  for j in range(3,-1,-1):
    if i==l:
      if j==3:
        dp[i][j]=1
      else:
        dp[i][j]=0
    else:
      if s[i]=='?':
        dp[i][j]=dp[i+1][j]*3
      else:
        dp[i][j]=dp[i+1][j]
      if j!=3 and (s[i]=='?' or s[i]==('abc'[j])):
        dp[i][j]+=dp[i+1][j+1]
    dp[i][j]%=mod
print(dp[0][0])
