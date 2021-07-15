from math import gcd
K=int(input())
g=0
for a in range(1,K-1):
  for b in range(a+1,K):
    for c in range(b+1,K+1):
      g+=gcd(gcd(a,b),c)*6
for  d in range(1,K):
  for e in range(d+1,K+1):
    g+=gcd(d,e)*6
g+=K*(K+1)//2
print(g)
