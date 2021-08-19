import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


""" どのパワー以上の組み合わせまで握手するのか二分探索で調べる
    同じパワーとなる組み合わせに注意 """
N, M = lr()
A = np.array(lr())
A.sort()


def check(x):
    # x以上の幸福度で握手した時、M回以下だとTrueを返す
    Y = np.searchsorted(A, x - A)
    return N * N - Y.sum() <= M


ok = 10 ** 6
ng = 0
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

Acum = np.zeros(N + 1, np.int64)
Acum[1:] = A.cumsum()
Y = np.searchsorted(A, ok - A)
answer = (Acum[-1] - Acum[Y]).sum() + (A * (N - Y)).sum()
answer += ng * (M - (N - Y).sum())
print(answer)
# 24
