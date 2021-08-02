import math
from functools import reduce
n = int(input())
a = [int(x) for x in input().split()]


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


print(my_gcd(*a))
