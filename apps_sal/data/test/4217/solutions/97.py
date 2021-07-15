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
    return a*b//math.gcd(a, b)

MOD = 10**9+7

# ============================================================

n, m = list(map(int, input().split()))

L = [0]*(m+1)

for i in range(n):
    A = list(map(int, input().split()))
    for k in range(1, A[0]+1):
        L[A[k]] += 1
print((L.count(n)))

