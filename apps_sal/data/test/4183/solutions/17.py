n = int(input())
t = [int(input()) for _ in range(n)]

import math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
print(lcm(*t))
