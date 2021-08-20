import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


n = int(input())
a = list(map(int, input().split()))
print(gcd_list(a))
