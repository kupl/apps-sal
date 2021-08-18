
import sys


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

N = INT()
N = format(N, '060b')[::-1]
N = [0] + list(map(int, N))

dp = list2d(61, 3, 0)
dp[60][0] = 1
for i in range(60, 0, -1):
    for j in range(3):
        for k in range(3):
            nxt = min(j * 2 + N[i] - k, 2)
            if nxt >= 0:
                dp[i - 1][nxt] += dp[i][j]
                dp[i - 1][nxt] %= MOD
print(((dp[0][0] + dp[0][1] + dp[0][2]) % MOD))
