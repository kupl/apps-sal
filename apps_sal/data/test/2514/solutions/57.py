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
A = list(map(int, input().split()))
q = int(input())

L = [0] * (10**5 + 1)

for i in range(n):
    L[A[i]] += 1
s = sum(A)

for i in range(q):
    a, b = list(map(int, input().split()))
    s += (b - a) * L[a]
    L[b] += L[a]
    L[a] = 0
    print(s)
