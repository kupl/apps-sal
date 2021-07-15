N,A,B=map(int, input().split())
D=list(map(int, input().split()))
D=sorted(D)[::-1]
import math
from math import comb
print(sum(D[:A])/A)
ans=0
if D[0]!=D[A-1]:
  n=D.count(D[A-1])
  k=D[:A].count(D[A-1])
  print(comb(n,k))
else:
  ans=0
  n=D.count(D[A-1])
  for i in range(A,min(n,B)+1):
    ans+=comb(n,i)
  print(ans)
