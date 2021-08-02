import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


N = int(input())
l = list(map(int, input().split()))

lcm = lcm_list(l)

ans = 0
for i in l:
    ans += (lcm - 1) % i
print(ans)
