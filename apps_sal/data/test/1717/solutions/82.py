import math
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
ans = 2
for i in range(3, n + 1):
    ans = lcm(ans, i)
print(ans + 1)
