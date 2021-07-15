N = int(input())
A = list(map(int,input().split()))

mod = pow(10,9)+7
ok = 1

import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

LCM = lcm_list(A)

import numpy as np
B = np.array(A)
C = LCM//B


print(sum(C)%mod)
