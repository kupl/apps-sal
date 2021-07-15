N,C=map(int, input().split())
D=[list(map(int, input().split())) for _ in range(C)]
c=[list(map(int, input().split())) for _ in range(N)]
C0=[0]*C
C1=[0]*C
C2=[0]*C
for i in range(N):
  for j in range(N):
    if (i+j)%3==0:
      C0[c[i][j]-1]+=1
    elif (i+j)%3==1:
      C1[c[i][j]-1]+=1
    else:
      C2[c[i][j]-1]+=1
      
import itertools
A=list(itertools.permutations(range(1,C+1),3))
ans=1000*250000
for a,b,c in A:
  d=0
  for i in range(C):
    d+=C0[i]*D[i][a-1]
    d+=C1[i]*D[i][b-1]
    d+=C2[i]*D[i][c-1]
  ans=min(ans,d)
print(ans)
