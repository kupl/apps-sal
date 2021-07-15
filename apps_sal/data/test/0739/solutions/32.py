import sys
from math import log10

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
INF = 10 ** 19
MOD = 10 ** 19 + 7
EPS = 10 ** -10

def bisearch_min(mn, mx, func):
    ok = mx
    ng = mn
    while ng+1 < ok:
        mid = (ok+ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def mat_pow(mat, init, K, MOD):
    """ 行列累乗 """

    def mat_dot(A, B, MOD):
        """ 行列の積 """

        if not isinstance(A[0], list) and not isinstance(A[0], tuple):
            A = [A]
        if not isinstance(B[0], list) and not isinstance(A[0], tuple):
            B = [[b] for b in B]
        n1 = len(A)
        n2 = len(A[0])
        _ = len(B)
        m2 = len(B[0])
        res = list2d(n1, m2, 0)
        for i in range(n1):
            for j in range(m2):
                for k in range(n2):
                    res[i][j] += A[i][k] * B[k][j]
                    res[i][j] %= MOD
        return res

    def _mat_pow(mat, k, MOD):
        """ 行列matをk乗する """

        n = len(mat)
        res = list2d(n, n, 0)
        for i in range(n):
            res[i][i] = 1
        while k > 0:
            if k & 1:
                res = mat_dot(res, mat, MOD)
            mat = mat_dot(mat, mat, MOD)
            k >>= 1
        return res

    res = _mat_pow(mat, K, MOD)
    res = mat_dot(res, init, MOD)
    return [a[0] for a in res]

L, a, b, M = MAP()

A = [0] * 20
for i in range(1, 20):
    x = 10 ** i
    # A[i] = bisearch_min(-1, L, lambda m: ceil(x-a, b) <= m)
    A[i] = max(min(ceil(x-a, b), L), 0)
C = [0] * 20
for i in range(1, 20):
    C[i] = A[i] - A[i-1]

init = [0, a, 1]
for d in range(1, 20):
    K = C[d]
    if K == 0:
        continue
    mat = [
        # dp0[i] = dp0[i-1]*10^d + dp1[i-1]*1 + 1*0
        [pow(10, d, M), 1, 0],
        # dp1[i] = dp0[i-1]*0 + dp1[i-1]*1 + 1*b
        [0, 1, b],
        # 1 = dp0[i-1]*0 + dp1[i-1]*0 + 1*1
        [0, 0, 1],
    ]
    res = mat_pow(mat, init, K, M)
    init[0] = res[0]
    init[1] = res[1]
ans = res[0]
print(ans)

# dp0 = [0] * (L+1)
# dp1 = [0] * (L+1)
# dp0[0] = 0
# dp1[0] = a
# for i in range(1, L+1):
#     dp0[i] = (dp0[i-1]*pow(10, int(log10(dp1[i-1]))+1, M) + dp1[i-1]) % M
#     dp1[i] = dp1[i-1] + b
# ans = dp0[-1]
# print(ans)

