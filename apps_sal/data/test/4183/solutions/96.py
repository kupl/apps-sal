import math
from functools import reduce

def lcm_base(x,y):
    return (x*y)//math.gcd(x,y)

def lcm_list(numbers):
    return reduce(lcm_base,numbers,1)

n=int(input())
nums=[int(input()) for i in range(n)]

print((lcm_list(nums)))

