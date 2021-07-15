# C - Multiple Clocks
import functools
import math
N = int(input())
T = [int(input()) for _ in range(N)]

def lcm(a,b):
    LCM = a*b//math.gcd(a,b)
    return LCM

def all_lcm(A):
    ans = functools.reduce(lcm,A,1)
    return ans

print(all_lcm(T))
