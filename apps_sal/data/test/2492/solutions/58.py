# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# neg, zero, posに分けて、二分探索
N, K = lr()
A = np.array(lr()); A.sort()
neg = A[A < 0]
zero = A[A == 0]
pos = A[A > 0]


def check(x):
    '''x以下の積がK個以上あるならTrueを返す'''
    cnt = 0  # 最後に２でわる
    if x >= 0:
        cnt += len(zero) * N
    cnt += (np.searchsorted(A, x // pos, side='right')).sum()
    cnt += (N - np.searchsorted(A, (-x - 1) // (-neg), side='right')).sum()
    cnt -= np.count_nonzero(A * A <= x)
    assert cnt % 2 == 0
    return (cnt // 2) >= K


ok = 10**18; ng = -10**18 - 1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
# 30
