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
k, n = list(map(int, input().split()))
A = list(map(int, input().split()))

m = 2 * 10**5
M = [0] * n
dist = min(A[n - 1] - A[0], k - A[n - 1] + A[0])
for i in range(n - 1):
    dist = max(dist, A[i + 1] - A[i])
print((k - dist))
