
import sys
from bisect import bisect_left
from itertools import accumulate


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
INF = 10 ** 18
MOD = 10 ** 9 + 7


def bisearch_min(mn, mx, func):

    ok = mx
    ng = mn
    while ng + 1 < ok:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok


M, N, K, T = MAP()
A = LIST()

LRD = []
for i in range(K):
    l, r, d = MAP()
    LRD.append((l, r, d))


def check(m):
    imos = [0] * (N + 2)
    for l, r, d in LRD:
        if d > m:
            imos[l] += 1
            imos[r + 1] -= 1
    imos = list(accumulate(imos))
    cnt = 0
    for i in imos:
        if i > 0:
            cnt += 1
    return cnt * 2 + N + 1 <= T


amx = max(A)
res = bisearch_min(0, amx + 1, check)
A.sort()
idx = bisect_left(A, res)
cnt = M - idx
print(cnt)
