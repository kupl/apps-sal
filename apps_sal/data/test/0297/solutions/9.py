#!/usr/bin/env python3
import sys
from math import gcd

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

n, m, k = rint()

if (2*n*m)%k:
    print("NO")
    return

nk_gcd = gcd(n, k)

w = n//nk_gcd
k = k//nk_gcd

mk_gcd = gcd(m, k)

h = m//mk_gcd
k = k//mk_gcd

if k == 1:
    if w < n:
        w *= 2
    elif h < m:
        h *= 2
else:
    # In order to 2*n*m/k is integer, k is 2, so no need to divide  w or h by 2
    pass

print("YES")
print(0, 0)
print(w, 0)
print(0, h)

