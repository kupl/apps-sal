
import sys
from copy import copy


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, Q = MAP()

imos = [0] * (N + 2)
Pts = [None] * Q
for i in range(Q):
    l, r = MAP()
    Pts[i] = (l, r)
    imos[l] += 1
    imos[r + 1] -= 1
for i in range(N + 1):
    imos[i + 1] += imos[i]

mx = 0
for i in range(Q):
    cp = copy(imos)
    l, r = Pts[i]
    for j in range(l, r + 1):
        cp[j] -= 1
    sm = 0
    cnt1 = [0] * (N + 2)
    for j in range(1, N + 1):
        if cp[j] > 0:
            sm += 1
        if cp[j] == 1:
            cnt1[j] += 1
        cnt1[j + 1] += cnt1[j]
    for j in range(i + 1, Q):
        l2, r2 = Pts[j]
        mx = max(mx, sm - (cnt1[r2] - cnt1[l2 - 1]))

print(mx)
