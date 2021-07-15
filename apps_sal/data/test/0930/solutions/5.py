M=10**9+7
n,k=map(int,input().split())
from functools import lru_cache
@lru_cache(None)
def f(x):
  if x: return x*f(x-1)%M
  return 1
l=[f(i) for i in range(n+1)]
a=0
for i in range(min(n,k+1)):
  c=l[n]*l[n-1]%M
  p=l[i]**2*l[n-i]*l[n-i-1]%M
  a+=c*pow(p,M-2,M)
print(a%M)
