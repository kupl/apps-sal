import sys
import math


def gcd(a, b):
    if(b == 0):
        return a
    r = a % b
    return gcd(b, r)


n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

vmin = min(an)
kmin = 101
for i in range(n):
    t = gcd(vmin, an[i])
    if(t < vmin):
        vmin = t

print(n * t)
