from collections import Counter
from math import prod

N,A,B=map(int,input().split())
v=list(map(int,input().split()))

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i

def comb(n,k):
    return factorial[n]*pow(factorial[n-k]*factorial[k], -1)
  
v = sorted(v,reverse=True)
  
if len(set(v[:A]))==1:
  print(v[0])
  ans=0
  for i in range(A,B+1):
    if i > 1 and v[i-1] != v[i-2]:break
    ans += comb(Counter(v)[v[0]],i)
  print(int(ans))
  return

print(sum(v[:A])/A)

c = Counter(v)
thr = v[A-1]

if c[thr] == 1 or v[A-1] != v[A]:
  res=[]
  for k in c.keys():
    if k >= thr:
      res.append(c[k])
    
  print(prod(res))
  return
  
res=[]
for k in c.keys():
  if k > thr:
    res.append(c[k])

ans=prod(res)

idx = v[:A].index(v[A-1])-1

print(int(ans*comb(c[v[A-1]],A-1-idx)))
