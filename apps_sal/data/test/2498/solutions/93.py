import math
import sys
from functools import reduce

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = A[i] // 2


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


C = lcm_list(A)
B = [0 for _ in range(N)]

for i in range(N):
    B[i] = C // A[i]
    if B[i] % 2 == 0:
        print(0)
        return

print((M // C + 1) // 2)
