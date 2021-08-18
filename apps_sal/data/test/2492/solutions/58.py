import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, K = lr()
A = np.array(lr())
A.sort()
neg = A[A < 0]
zero = A[A == 0]
pos = A[A > 0]


def check(x):
    '''x以下の積がK個以上あるならTrueを返す'''
    cnt = 0
    if x >= 0:
        cnt += len(zero) * N
    cnt += (np.searchsorted(A, x // pos, side='right')).sum()
    cnt += (N - np.searchsorted(A, (-x - 1) // (-neg), side='right')).sum()
    cnt -= np.count_nonzero(A * A <= x)
    assert cnt % 2 == 0
    return (cnt // 2) >= K


ok = 10**18
ng = -10**18 - 1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
