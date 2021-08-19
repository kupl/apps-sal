import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


n = input()
l = [int(x) for x in input().split()]
print(gcd_list(l))
