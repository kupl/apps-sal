n,k=list(map(int,input().split()))
lr=[]
for i in range(k):
  l_,r_=list(map(int,input().split()))
  lr.append([l_,r_])

dp=[0]*(n+1)
sdp=[0]*(n+1)
dp[1]=1
sdp[1]=1
p=998244353
for i in range(2,n+1):
  for l,r in lr:
    if i-l>=1:
      if i-r>=1:
        dp[i]=(dp[i]+sdp[i-l]-sdp[i-r-1])%p
      else:
        dp[i]=(dp[i]+sdp[i-l])%p
  sdp[i]=(sdp[i-1]+dp[i])%p

print((dp[n]%p))


