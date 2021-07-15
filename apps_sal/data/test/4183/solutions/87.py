n=int(input())

import math
from functools import reduce
def lcm_base(x, y):# 最小公倍数
    return (x * y) // math.gcd(x, y)
def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

t=[]
for i in range(n):
    t.append(int(input()))

print(lcm(t))
