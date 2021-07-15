n,k=map(int,input().split())
p=list(map(int,input().split()))
t=input()
s='rsp'
dp=[[-10**10]*(n+k) for _ in range(3)]
for i in range(k):
  for j in range(3):
    dp[j][i]=0
for i in range(n):
  for j in range(3):
    for l in range(3):
      if j==l:
        continue
      res=((s.index(t[i])-l+3)%3==1)*p[l]
      if dp[l][i+k]<dp[j][i]+res:
        dp[l][i+k]=dp[j][i]+res
ans=0
for i in range(n,n+k):
  ans+=max(dp[0][i],dp[1][i],dp[2][i])
print(ans)
