# import numpy as np
# import math

# from scipy.special import perm
# from scipy.special import comb

# from numba import njit
# @njit('f8(i8,i8,i8,i8,f8[:,:,:])', cache=True)

def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10**9 + 7


H, W = list(map(int, input().split()))
h, w = list(map(int, input().split()))
print(((H - h) * (W - w)))
