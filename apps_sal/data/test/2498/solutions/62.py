import math
from functools import reduce
(N, M) = list(map(int, input().split()))
A = [int(x) // 2 for x in input().split()]


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


LCM = lcm(*A)
for a in A:
    if LCM // a % 2 == 0:
        print(0)
        break
else:
    print((M // LCM + 1) // 2)
