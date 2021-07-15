n,W=map(int,input().split())
w=[0 for i in range(n)]
v=[[] for i in range(4)]
dp=[[0] for i in range(4)]
for i in range(n):
  w[i],vi=map(int,input().split())
  v[w[i]-w[0]].append(vi)
for i in range(4):
  v[i].sort(reverse=True)
  for j in v[i]:
    dp[i].append(dp[i][-1]+j)
def dfs(i,cost):
  if cost>W:
    return -10**10
  elif i==4:
    return 0
  else:
    val=0
    for j in range(len(dp[i])):
      val=max(val,dp[i][j]+dfs(i+1,cost+j*(w[0]+i)))
    return val
print(dfs(0,0))
