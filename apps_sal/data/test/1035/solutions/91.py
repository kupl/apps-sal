from math import *
g = gcd(*map(int,input().split()))
D = {}
n = 2

while n*n<=g:
  if g%n:
    n+=1
  else:
    g//=n
    D[n]=D.get(n,0)+1

if 1<g:
  D[g]=D.get(g,0)+1

print(len(D)+1)
