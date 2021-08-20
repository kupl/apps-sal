import math
from functools import reduce
N = int(input())
A = list(map(int, input().split()))


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


print(gcd_list(A))
