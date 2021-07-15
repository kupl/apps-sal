n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
from math import gcd
ans=a[0]
for i in range(1,n):
  ans=ans*a[i]//gcd(ans,a[i])
s=sum(pow(x,mod-2,mod) for x in a)
print((s*ans%mod))

