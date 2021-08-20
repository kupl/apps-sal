import numpy as np
MOD = 998244353
(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))
coefs = np.array([0] * (S + 1))
coefs[0] = 1
for i in range(N):
    tmp = coefs[:]
    coefs = coefs * 2
    coefs[A[i]:] += tmp[:-A[i]]
    coefs %= MOD
print(coefs[-1])
