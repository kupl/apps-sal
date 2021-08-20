import math
from functools import reduce


def gcd(list):
    return reduce(math.gcd, list)


(n, x) = map(int, input().split())
a = map(lambda b: abs(int(b) - x), input().split())
print(gcd(a))
