def gcd(a, b):
    if b==0:
        return a
    return gcd(b,a%b)

def red(frac):
    gcdfrac = gcd(frac[0],frac[1])
    return (frac[0] // gcdfrac, frac[1] // gcdfrac)

def add(i, frac):
    a,b = frac
    a += b * i
    return red((a,b))

import sys
args = list(map(int, sys.stdin.read().split()))
p, q = args[0], args[1]
n = args[2]
s = (args[2+n],1)
for i in range(0,n-1):
    s = add(args[1+n-i] , (s[1],s[0]))
if(s == red((p,q))):
    print('YES')
else:
    print('NO')
