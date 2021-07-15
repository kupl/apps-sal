X, Y =list(map(int, input().split()))
mod = 1000000007

import sys
if (X + Y) % 3 != 0:
    print((0))
    return
offset = (X+Y)//3
X, Y = X-offset, Y-offset

if X<0 or Y<0:
    print((0))
    return
    
X, Y = max(X, Y), min(X, Y)

def C(n, r, mod):
    num = 1
    den = 1
    for i in range(r):
        num*=n-i
        num%=mod
        den*=i+1
        den%=mod
    return (num*pow(den, mod-2, mod))%mod

print((C(X+Y, Y, mod)))

