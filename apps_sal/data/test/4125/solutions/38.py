from math import *

N,X=list(map(int,input().split()))
x=list(map(int,input().split()))
ans=0
for i in x:
  ans=gcd(ans,abs(i-X))
print(ans)

