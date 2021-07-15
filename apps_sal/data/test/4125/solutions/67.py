n,x=map(int,input().split())
X=list(map(int,input().split()))
for i in range(n):
  X[i]=abs(X[i]-x)
from math import gcd
ans=X[0]
for i in range(1,n):
  ans=gcd(ans,X[i])

print(ans)
