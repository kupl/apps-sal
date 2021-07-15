from collections import deque
f=lambda:list(map(int,input().split()))
r=range
n,m,k=f()
F=[deque([])for _ in r(n)]
A=[0]*n
B=[-1]*n
C=[-1]*n
Q=deque([])
for _ in r(m):a,b=f();a-=1;b-=1;F[a].append(b);F[b].append(a);A[a]+=1;A[b]+=1
for i in r(n):
  Q.append(x:=i)
  y=0
  while Q:
    z=Q.popleft()
    if B[z]>-1:continue
    B[z]=x
    Q.extend(F[z])
    y+=1
  C[x]=y
D=[[B[i],C[B[i]]-A[i]-1]for i in r(n)]
for _ in r(k):
  c,d=f()
  c,d=c-1,d-1
  if D[c][0]==D[d][0]:D[c][1]-=1;D[d][1]-=1
print((*[d[1] for d in D]))

