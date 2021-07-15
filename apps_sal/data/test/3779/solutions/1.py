import math
n,k=map(int,input().split())
g=k
for a in map(int,input().split()):
 g=math.gcd(g,a)
print(k//g)
print(*range(0,k,g))
