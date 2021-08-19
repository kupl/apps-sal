import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
t = [int(input()) for _ in range(n)]
print(lcm(*t))
