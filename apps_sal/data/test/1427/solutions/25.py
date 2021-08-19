import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())
a = list(map(int, input().split()))
l = lcm(*a)
MOD = 10 ** 9 + 7
ans = 0
for i in range(n):
    ans += l // a[i]
print(ans % MOD)
