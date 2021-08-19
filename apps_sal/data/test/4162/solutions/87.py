import math
from functools import reduce


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(list):
    return reduce(lcm_base, list, 1)


n = int(input())
a = list(map(int, input().split()))
l = lcm(a) - 1
ans = 0
for i in range(n):
    ans += l % a[i]
print(ans)
