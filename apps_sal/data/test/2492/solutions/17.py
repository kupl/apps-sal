import numpy as np
N, K = map(int, input().split())
L = np.array(list(map(int, input().split())))

L = np.sort(L)
pos = L[0 < L]
neg = L[0 > L]
zero = len(L[L == 0])


def f(x):
    tmp = 0
    if x >= 0:
        tmp += zero * N
    tmp += np.searchsorted(L, x // pos, side='right').sum()
    tmp += (N - np.searchsorted(L, -(-x // neg), side='left')).sum()
    tmp -= np.count_nonzero(L * L <= x)
    return tmp // 2


l, r = -10**18, 10**18
while l < r - 1:
    m = (l + r) // 2
    count = f(m)
    if count >= K:
        r = m
    else:
        l = m

print(r)
