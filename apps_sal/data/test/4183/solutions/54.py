import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())

l = []

for i in range(n):
    t = int(input())
    l.append(t)

print((lcm_list(l)))
