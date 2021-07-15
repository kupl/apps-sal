N,Ma,Mb=list(map(int,input().split()))
ABC=[tuple(map(int,input().split())) for i in range(N)]
inf=float("inf")
DP=[[inf]*401 for i in range(401)]
DP[0][0]=0
for a,b,c in ABC:
   for i in reversed(range(401)):
      for j in reversed(range(401)):
         if DP[i][j]!=inf:
            DP[i+a][j+b]=min(DP[i][j]+c,DP[i+a][j+b])
ans=inf
for i in range(1,401):
   for j in range(1,401):
      if Ma*j==Mb*i:
         ans=min(ans,DP[i][j])
print(-1 if ans==inf else ans)
