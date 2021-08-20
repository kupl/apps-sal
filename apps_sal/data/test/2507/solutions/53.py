import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, K) = lr()
A = np.array(lr())
A.sort()
F = np.array(lr())
F.sort()
F = F[::-1]


def check(x):
    limit = x // F
    Y = A - limit
    if np.any(Y > K):
        return False
    cost = Y[Y >= 0].sum()
    if cost <= K:
        return True
    else:
        return False


ok = 10 ** 15
ng = -1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
