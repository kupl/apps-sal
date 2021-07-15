H,W=map(int,input().split())
C=[list(map(int,input().split())) for _ in range(10)]
d=[0]*10
for _ in range(H):
  for i in list(map(int,input().split())):
    if i>=0: d[i]+=1
r=range(10)
for k in r:
  for i in r:
    for j in r:
      C[i][j]=min(C[i][j],C[i][k]+C[k][j])

print(sum(C[i][1]*d[i] for i in r))
