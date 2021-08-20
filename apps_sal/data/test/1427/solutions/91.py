from math import gcd
from functools import reduce
N = int(input())
A = [int(i) for i in input().split()]
mod = 10 ** 9 + 7


def lcm_base(x, y):
    return x * y // gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


num = lcm_list(A) % mod
ans = 0
for a in A:
    ans += num * pow(a, mod - 2, mod) % mod
ans %= mod
print(ans)
