from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations
from sys import stdin
nii=lambda:map(int,stdin.readline().split())

n,m,r=nii()
r=list(nii())

s=[[float('inf')]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    s[i][j]=0
for i in range(m):
  a,b,c=nii()
  a-=1
  b-=1
  s[a][b]=c
  s[b][a]=c

ws=floyd_warshall(s)

ans=10**9
for i in permutations(r):
  t_ans=0
  for j in range(1,len(i)):
    t_ans+=ws[i[j-1]-1][i[j]-1]
  ans=min(ans,t_ans)
print(int(ans))
