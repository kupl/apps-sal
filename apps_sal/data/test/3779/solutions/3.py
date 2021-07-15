from math import gcd
n,k=map(int,input().split())
g=0
l=list(map(int,input().split()))
for e in l:
    g=gcd(g,gcd(e,k))
print(k//g)
for i in range(0,k,g): print(i,end=' ')
