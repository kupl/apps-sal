n,k=list(map(int,input().split()))
m=998244353

P=[-1]*n

def find(x):
  if P[x]<0:
    return x
  P[x]=find(P[x])
  return P[x]

def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return

  if P[x]>P[y]:
    P[y]+=P[x]
    P[x]=y
  else:
    P[x]+=P[y]
    P[y]=x

def f(n):
  a=1
  while n>0:
    a*=n
    n-=1
  return a

A=[[int(c) for c in input().split()] for r in range(n)]

for r1 in range(n):
  for r2 in range(r1+1,n):
    for c in range(n):
      if A[r1][c]+A[r2][c]>k:
        break
    else:
      unite(r1,r2)

a=1
for r in range(n):
  if P[r]<0:
    a=(a*f(-P[r]))%m

P=[-1]*n
for c1 in range(n):
  for c2 in range(c1+1,n):
    for r in range(n):
      if A[r][c1]+A[r][c2]>k:
        break
    else:
      unite(c1,c2)

for c in range(n):
  if P[c]<0:
    a=(a*f(-P[c]))%m

print(a)

