h,w=list(map(int,input().split()))
a=[list(map(int,input().split()))for _ in range(h)]
b=[list(map(int,input().split()))for _ in range(h)]
d=[[a[i][j]-b[i][j]for j in range(w)]for i in range(h)]
dp=[w*[0]for _ in range(h)]
dp[0][0]=1<<(80+d[0][0])|1<<(80-d[0][0])
for i in range(h):
  for j in range(w):
    if i!=0:
      dp[i][j]|=(dp[i-1][j]<<80+d[i][j])
      dp[i][j]|=(dp[i-1][j]<<80-d[i][j])
    if j!=0:
      dp[i][j]|=(dp[i][j-1]<<80+d[i][j])
      dp[i][j]|=(dp[i][j-1]<<80-d[i][j])
n=dp[-1][-1]|(1<<15000)
ans=1<<1000
for i in range(15000):
  if n&(1<<i):ans=min(ans,abs(i-(h+w-1)*80))
print(ans)

