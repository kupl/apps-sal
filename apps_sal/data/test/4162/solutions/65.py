from functools import reduce
from math import gcd
n = int(input())
L = list(map(int, input().split()))


def lcm(x, y):
    return x * y // gcd(x, y)


a = reduce(lcm, L)
ans = 0
for i in range(n):
    ans += (a - 1) % L[i]
print(ans)
