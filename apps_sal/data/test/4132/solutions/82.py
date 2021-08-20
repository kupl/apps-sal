import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
a = [int(i) for i in input().split()]
if 1 in a:
    ans = 1
else:
    ans = gcd_list(a)
print(ans)
