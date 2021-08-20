import sys
from functools import reduce
import math


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
saisyo_koubaisu = lcm_list(a)
ans = 0
for aa in a:
    ans += (saisyo_koubaisu - 1) % aa
print(ans)
