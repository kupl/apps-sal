import sys
import numpy as np
from operator import itemgetter


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7
(N, T) = MAP()
AB = []
for i in range(N):
    (a, b) = MAP()
    AB.append((a, b))
AB.sort(key=itemgetter(0))
TMAX = 6007
dp = np.zeros((N + 1, TMAX), dtype=np.int64)
for i in range(N):
    (a, b) = AB[i]
    dp[i + 1] = dp[i]
    dp[i + 1, a:a + T] = np.maximum(dp[i + 1, a:a + T], dp[i, :T] + b)
print(dp[N].max())
