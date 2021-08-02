from functools import reduce
import math
n = int(input())
A = list(map(int, input().split()))


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


g = gcd_list(A)
print(g)
