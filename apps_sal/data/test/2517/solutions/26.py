
import sys

from scipy.sparse.csgraph import floyd_warshall


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

N, M, R = MAP()
A = [a - 1 for a in LIST()]
G = list2d(N, N, INF)
for i in range(M):
    a, b, c = MAP()
    a -= 1
    b -= 1
    G[a][b] = c
    G[b][a] = c

wf = floyd_warshall(G)

ans = INF
for r in range(R):
    dp = list2d(1 << R, R, INF)
    dp[1 << r][r] = 0
    for bit in range(1, (1 << R) - 1):
        for i in range(R):
            if not (bit >> i & 1):
                continue
            for j in range(R):
                if bit >> j & 1:
                    continue
                a, b = A[i], A[j]
                dp[bit | 1 << j][j] = min(dp[bit | 1 << j][j], dp[bit][i] + int(wf[a, b]))
    ans = min(ans, min(dp[-1]))
print(ans)
