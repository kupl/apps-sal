import math
import numpy as np
n, a, b = map(int, input().split())
mod = 10**9 + 7
factna = [n]
factnb = [n]
facta = [a]
factb = [b]

for i in range(1, a):
    factna.append(factna[-1] * (n - i) % mod)
    facta.append(facta[-1] * (a - i) % mod)

for i in range(1, b):
    factnb.append(factnb[-1] * (n - i) % mod)
    factb.append(factb[-1] * (b - i) % mod)


def pow(x, n):
    a = 1
    while(n > 0):
        if n % 2 == 1:
            a *= x % mod
        x *= x % mod
        n >>= 1
    return a


A = pow(2, n) % mod
B = factna[-1] * pow(facta[-1], mod - 2) % mod
C = factnb[-1] * pow(factb[-1], mod - 2) % mod
# print(factna,factb)
print((A - B - C - 1) % mod)
