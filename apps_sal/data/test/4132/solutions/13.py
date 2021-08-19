import sys
import math


def inint():
    return int(sys.stdin.readline())


def inintm():
    return list(map(int, sys.stdin.readline().split()))


def inintl():
    return list(inintm())


def instrm():
    return list(map(str, sys.stdin.readline().split()))


def instrl():
    return list(instrm())


n = inint()
A = inintl()
m = min(A)
mod_min = 10 ** 9
for a in A:
    if a % m == 0:
        continue
    mod_min = min(mod_min, a % m)
if mod_min == 10 ** 9:
    print(m)
else:
    print(math.gcd(m, mod_min))
