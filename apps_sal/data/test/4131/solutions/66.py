N,M=map(int,input().split())
A=[[] for i in range(N)]
for i in range(M):
  a,b=map(int,input().split())
  A[a-1].append((b,i))
ans=[0]*M
for i in range(N):
  d=sorted(A[i])
  n=len(d)
  for j in range(n):
    a,b=d[j]
    D=str(i+1)
    E=str(j+1)
    r=D.zfill(6)+E.zfill(6)
    ans[b]=r
for i in ans:
  print(i)
