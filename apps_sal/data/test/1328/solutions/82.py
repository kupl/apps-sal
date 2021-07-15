inf=10**10
n,ma,mb=map(int,input().split())
abc=[list(map(int,input().split())) for _ in range(n)]
memo=[[inf]*401 for _ in range(401)]
memo[0][0]=0
for a,b,c in abc:
  for i in range(400,-1,-1):
    for j in range(400,-1,-1):
      if memo[i][j]!= inf :
        memo[i+a][j+b]= min(memo[i+a][j+b], memo[i][j] + c)


ans=inf
for i in range(1,min(400//ma,400//mb)):
  ans=min(ans, memo[ma*i][mb*i])

if ans==inf:
  print(-1)
else:
  print(ans)
