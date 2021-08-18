import sys
from math import log2, floor, ceil, sqrt


def Ri(): return [int(x) for x in sys.stdin.readline().split()]
def ri(): return sys.stdin.readline().strip()


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


INF = 10 ** 18
MOD = 10**9 + 7

n = int(ri())
arr = Ri()
a = sorted(arr)
dic = {}
ite = 1
for i in range(n):
    if a[i] not in dic:
        dic[a[i]] = ite
        ite += 1
for i in range(n):
    arr[i] = dic[arr[i]]
dp = list2d(n, n + 1, 0)
for i in range(n):
    for j in range(n + 1):
        dp[i][j] = 1
maxx = 1
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        dp[i][arr[j]] = max(dp[i][arr[j]], dp[j][arr[i]] + 1)
        maxx = max(maxx, dp[i][arr[j]])
print(maxx)
