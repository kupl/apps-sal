import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


n, m = list(map(int, input().split()))
a_pr = [i // 2 for i in list(map(int, input().split()))]
lcm_ = lcm_list(a_pr)
res, div2 = 0, None
for ai in a_pr:
    cnt = 0
    while ai % 2 == 0:
        ai //= 2
        cnt += 1
    if div2 is None:
        div2 = cnt
    elif cnt != div2:
        print((0))
        return

print((int(my_round(m // lcm_ / 2))))

