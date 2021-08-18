import numpy as np
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

L, A, B, M = list(map(int, input().split()))

C = []
for i in range(19):
    C.append(min(max(0, (10**i - A - 1) // B + 1), L))


def R_mul(A, B, M):
    return np.mod((np.dot(A, B)), M)


def R_pow(R, n, M):
    if n == 1:
        return R

    R2 = R_mul(R, R, M)
    R2 = R_pow(R2, n // 2, M)

    if n % 2 == 0:
        return R2
    else:
        return R_mul(R2, R, M)


ans = 0
R = np.ones((3, 3))
s = np.array([0, A % M, 1])

for d in range(1, 19):
    r = C[d] - C[d - 1]
    if (0 == r):
        continue
    R0 = np.array([[pow(10, d, M), 1, 0], [0, 1, (B % M)], [0, 0, 1]])
    R = R_pow(R0, r, M)
    s = R_mul(R, s, M)
    if (C[d] > L):
        break

print((s[0]))
