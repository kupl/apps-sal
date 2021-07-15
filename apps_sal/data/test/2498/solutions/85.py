from math import gcd, ceil
from functools import reduce
import sys

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N, M = map(int, input().split())
a = [int(i)//2 for i in input().split()]

s = set()
for x in a:
    cur = 0
    y = x
    while y%2 == 0:
        cur += 1
        y //= 2
    s.add(cur)
    if len(s) >= 2:
        print(0)
        return
lcm = lcm_list(a)
print((M//lcm+1)//2)
