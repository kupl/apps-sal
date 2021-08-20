from math import *


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


(x, y, a, b) = list(map(int, input().split()))
nok = x * y // gcd(x, y)
a += (nok - a % nok) % nok
b -= b % nok
print((b - a) // nok + 1)
