import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
AA = [int(input()) for i in range(N)]
print(lcm(*AA))
