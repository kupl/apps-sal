S=int(input())
mod=10**9+7

dp=[0]*(S+1)
dp[0]=1
for i in range(3,S+1):
  for j in range(0,(i-3)+1):
    dp[i]+=dp[j]
    dp[i]%=mod
print((dp[S]))

