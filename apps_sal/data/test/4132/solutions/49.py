import math
from functools import reduce


def gcd(*n):
    return reduce(math.gcd, n)


n = int(input())
*a, = map(int, input().split())
print(gcd(*a))
