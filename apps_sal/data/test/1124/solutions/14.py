from functools import reduce
from math import gcd

# 最大公約数


def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)

# 最小公倍数


def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)


n = int(input())
al = list(map(int, input().split()))
print(gcd_list(al))
