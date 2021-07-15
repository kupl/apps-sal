S=input()
mod=10**9+7
dp=[0]*13
dp[0]=1
for i in range(len(S)):
  if S[i]=='?':
    dp=[sum(dp[4*(j-k)%13] for k in range(10))%mod for j in range(13)]
  else:
    a=int(S[i])
    dp=[dp[4*(j-a)%13]%mod for j in range(13)]
print(dp[5])
