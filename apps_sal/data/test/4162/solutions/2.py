import math
from functools import reduce
N = int(input())
a = list(map(int, input().split()))


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


m = lcm_list(a) - 1
f = sum([m % item for item in a])
print(f)
