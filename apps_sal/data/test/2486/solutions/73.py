
import sys
import numpy as np


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7


def bisearch_min(mn, mx, func):
    """ 条件を満たす最小値を見つける二分探索 """

    ok = mx
    ng = mn
    while ng + 1 < ok:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, K = MAP()
A = LIST()


def check(omit):
    dp = np.zeros((N + 1, K), dtype=np.bool)
    dp[0, 0] = 1
    for i in range(N):
        dp[i + 1] |= dp[i]
        if i != omit and A[i] < K:
            dp[i + 1, A[i]:] |= dp[i, :K - A[i]]
    for j in range(max(0, K - A[omit]), K):
        if dp[N, j]:
            return True
    return False


A.sort()
print((bisearch_min(-1, N, check)))
