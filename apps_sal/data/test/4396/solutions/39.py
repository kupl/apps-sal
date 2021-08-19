# import numpy as np
# import math

# from scipy.special import perm : perm(n, r, exact=True)
# from scipy.special import comb : comb(n, r, exact=True)

# import itertools
# for v in itertools.combinations(L, n):M.append(list(v))

# from numba import njit
# @njit('f8(i8,i8,i8,i8,f8[:,:,:])', cache=True)


""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10**9 + 7

# ============================================================

n = int(input())
ans = 0
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == 'JPY':
        ans += x
    else:
        ans += x * 380000
print(ans)
