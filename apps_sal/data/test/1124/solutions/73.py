from functools import reduce
import math
n = int(input())
l = list(map(int, input().split()))


def gcd_list(numbers: list) -> int:
    return reduce(math.gcd, numbers)


print((gcd_list(l)))
