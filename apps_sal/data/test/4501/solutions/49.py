f=lambda:map(int,input().split())
n,a=f()
l=[i-a for i in f()]
dp=[[0]*5000 for _ in range(51)]
Z=2500
dp[0][Z]=1
for i in range(n):
  for s in range(5000-max(l[i],0)):
    dp[i+1][s]+=dp[i][s]
    dp[i+1][s+l[i]]+=dp[i][s]
print(dp[n][Z]-1)
