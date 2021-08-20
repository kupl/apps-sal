import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(list):
    return reduce(lcm_base, list, 1)


N = int(input())
T = [int(input()) for i in range(N)]
print(lcm_list(T))
