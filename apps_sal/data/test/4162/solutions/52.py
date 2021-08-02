import math
from functools import reduce


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm, numbers, 1)


N = int(input())
A = list(map(int, input().split()))

MOD = lcm_list(A) - 1

ans = 0
for a in A:
    ans += MOD % a
print(ans)
