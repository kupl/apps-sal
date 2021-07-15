l, n, m = map(int, input().split())
from fractions import gcd
lcm = lambda x, y: x // gcd(x,y) * y
u = lcm(n,m)
v = min(n,m)
a = (l//u) * v + min(v, l%u+1) - 1    
print(a//gcd(a,l),'/',l//gcd(a,l),sep='')


