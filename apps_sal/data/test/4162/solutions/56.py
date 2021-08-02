from math import gcd
from functools import reduce


def lcm(x, y):
    return x * y // gcd(x, y)


N, *A = list(map(int, open(0).read().split()))
l = reduce(lcm, A) - 1
print((sum(l % a for a in A)))
