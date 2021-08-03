import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def __starting_point():
    N = int(input())
    n = [i for i in range(2, N + 1)]
    print(lcm_list(n) + 1)


__starting_point()
