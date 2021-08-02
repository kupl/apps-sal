import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
lst = [i for i in range(2, n + 1)]
print(lcm_list(lst) + 1)
