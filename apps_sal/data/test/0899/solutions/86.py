n,m=map(int,input().split())
INF=10**18
e=[[INF for _ in range(n)]for _ in range(n)]
d=[]
for i in range(m):
  a,b,c=map(int,input().split())
  e[a-1][b-1]=c
  e[b-1][a-1]=c
  d.append((a-1,b-1,c))
for k in range(n):
  for i in range(n):
    for j in range(n):
      e[i][j]=min(e[i][j],e[i][k]+e[k][j])
ans=0
for i,j,k in d:
  if e[i][j]!=k:ans+=1
print(ans)
