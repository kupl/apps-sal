import math
from functools import reduce

n = int(input())
t = [int(input()) for _ in range(n)]


def lcm(a, b):
    return a * b // math.gcd(a, b)


print(reduce(lcm, t))
