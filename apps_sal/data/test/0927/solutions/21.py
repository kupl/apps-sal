n,m=map(int,input().split())
a=list(map(int,input().split()))
temp=[0,2,5,5,4,5,6,3,7,6]
dp=[-1]*(n+1)
dp[0]=0
for i in range(n+1):
  for j in a:
    if i+temp[j]<n+1:
      dp[i+temp[j]]=max(dp[i+temp[j]],dp[i]*10+j)
print(dp[n])
