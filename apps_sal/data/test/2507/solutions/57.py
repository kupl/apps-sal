import numpy as np
N, K = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.int64)
F = np.array(input().split(), dtype=np.int64)
A = np.sort(A)
F = np.sort(F)
F = F[::-1]


def C(m):
    need = m // F
    cost = A - need
    cost[cost < 0] = 0
    return cost.sum() <= K


l, r = -1, 10 ** 18 + 10
while r - l > 1:
    m = (r + l) // 2
    if C(m):
        r = m
    else:
        l = m

print(r)

