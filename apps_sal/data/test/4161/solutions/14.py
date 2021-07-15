from math import *

K=int(input())
ans=0
for i in range(1,K+1):
  for j in range(1,K+1):
    for k in range(1,K+1):
      ans+=gcd(k,gcd(i,j))
print(ans)

