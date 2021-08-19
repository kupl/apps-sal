import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
numList = list(range(2, N + 1))
ans = lcm_list(numList) + 1
print(ans)
