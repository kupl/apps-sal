import sys
from collections import Counter


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

for _ in range(INT()):
    N = INT()
    A = LIST()

    swapped = (N % 2 == 1)
    C = Counter(A)
    is_0 = True
    for v in list(C.values()):
        if v % 2 != 0:
            is_0 = False
            break

    if swapped ^ (not is_0):
        print('First')
    else:
        print('Second')
