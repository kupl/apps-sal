from functools import reduce
from math import gcd


def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)


def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)


n = int(input())
al = list(map(int, input().split()))
print(gcd_list(al))
