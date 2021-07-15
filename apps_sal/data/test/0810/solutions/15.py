def R(): return list(map(int, input().split()))
def I(): return int(input())
def S(): return str(input())

def L(): return list(R())

from collections import Counter 

import math
import sys

from itertools import permutations


import bisect

mod=10**9+7

#print(bisect.bisect_right([1,2,3],2))
#print(bisect.bisect_left([1,2,3],2))

a,b,n=R()

fact=[1]*(n+1)

for i in range(1,n+1):
    fact[i]=fact[i-1]*i
    fact[i]%=mod

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def check(val,a,b):
    while val>0:
        if val%10!= a and val%10!=b:
            return False

        val//=10

    return True

ans=0
for i in range(n+1):
    if check(a*i+b*(n-i),a,b):
        ans+=fact[n]*modinv((fact[i]*fact[n-i])%mod,mod)
        ans%=mod


print(ans)

