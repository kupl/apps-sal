from functools import reduce
import math


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
n_list = []
for i in range(n - 1):
    n_list.append(i + 2)
print(lcm_list(n_list) + 1)
