import numpy as np
# import math

# from scipy.special import perm
# from scipy.special import comb

# from numba import njit
# @njit('f8(i8,i8,i8,i8,f8[:,:,:])', cache=True)

def lcm(a, b):
    return a*b//math.gcd(a, b)

MOD = 10**9+7

n ,m, c = list(map(int, input().split()))

B = np.zeros(m)
A = np.zeros((n, m))


B = np.array(list(map(int, input().split())))

for i in range(n):
    A[i] = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if np.dot(A[i],B)+c > 0:
        cnt += 1
print(cnt)

