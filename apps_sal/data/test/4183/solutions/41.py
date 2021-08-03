import math
from functools import reduce


n = int(input())
tt = [int(input()) for i in range(n)]

x = 1


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


print(lcm(*tt))
