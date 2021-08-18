
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
INF = 10 ** 18
MOD = 10 ** 9 + 7

X, Y = MAP()

memo = list2d(1007, 1007, -1)


def rec(x, y):
    if memo[x][y] != -1:
        return memo[x][y]
    if x < 2 and y < 2:
        memo[x][y] = 0
        return 0
    res = 0
    for i in range(2, x + 1):
        if not rec(x - i, y + i // 2):
            res = 1
    for i in range(2, y + 1):
        if not rec(x + i // 2, y - i):
            res = 1
    memo[x][y] = res
    return res


if abs(X - Y) >= 2:
    print('Alice')
else:
    print('Brown')
