n,k=list(map(int,input().split()))

dp=[0]*(2*n+1) # 0,1,2~2n


for ii in range(1,n+1):
  # dp[2]~dp[n]
  dp[ii+1]=ii # ii+1 = [1,2,...,ii] + [ii,ii-1,...,1]
  # dp[n+1]~dp[n+n]
  dp[ii+n]=n-ii+1 # n+ii = [ii,ii+1,...,n] + [n,n-1,...,ii]

r=0
for ab in range(2,2*n+1):
  cd = ab - k # k=ab-cd
  if cd > 1 and cd <= 2*n:
    r+=dp[ab]*dp[cd]
print(r)

