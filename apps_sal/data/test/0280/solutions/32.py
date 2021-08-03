import sys
from itertools import permutations, accumulate
from bisect import bisect_left


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c for j in range(b)] for i in range(a)]
def list3d(a, b, c, d): return [[[d for k in range(c)] for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e for l in range(d)] for k in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10**9)
INF = 10**19
MOD = 10**9 + 7
EPS = 10**-10

N, M = MAP()
W = LIST()
VL = [(0, 0)]
for i in range(M):
    l, v = MAP()
    VL.append((v, l))

VL.sort()
V = [0] * (M + 1)
L = [0] * (M + 1)
for i in range(1, M + 1):
    V[i] = VL[i][0]
    L[i] = max(VL[i][1], L[i - 1])

if max(W) > min(V[1:]):
    print((-1))
    return

ans = INF
for perm in permutations(W):
    acc = [0] + list(accumulate(perm))
    dp = [0] * N
    for l in range(N):
        for r in range(l + 1, N):
            sm = acc[r + 1] - acc[l]
            idx = bisect_left(V, sm) - 1
            dp[r] = max(dp[r], dp[l] + L[idx])
    ans = min(ans, dp[N - 1])
print(ans)
