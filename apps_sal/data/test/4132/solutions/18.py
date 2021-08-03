import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


n = int(input())
print(gcd_list(list(map(int, input().split()))))
