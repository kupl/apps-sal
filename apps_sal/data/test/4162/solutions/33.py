import math
from functools import reduce
n = int(input())
A = list(map(int, input().split()))


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


ans = 0
lcm = lcm(*A)
for a in A:
    ans += (lcm - 1) % a
print(ans)
