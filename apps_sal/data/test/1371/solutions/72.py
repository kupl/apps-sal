n=int(input())
mod=10**9+7
dp=[0]*2001
dp[0]=1
sdp=[0]*2001
sdp[0]=1
for i in range(2000):
  dp[i+1]=sdp[i-2]
  sdp[i+1]=dp[i+1]+sdp[i]
print(dp[n]%mod)
