# -*- coding: utf-8 -*-

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

N = INT()
A = LIST()

l = 1
m = 2
r = 3
a = sum(A[:l])
b = sum(A[l:m])
c = sum(A[m:r])
d = sum(A[r:])
ans = max(a, b, c, d) - min(a, b, c, d)
# 尺取法(3点動かす)
while m < N - 1:
    # a,bの差が最小になるまで左を動かす
    while l < m - 1 and abs(a - b) > abs(a + A[l] - (b - A[l])):
        a += A[l]
        b -= A[l]
        l += 1
    # c,dの差が最小になるまで右を動かす
    while r < N - 1 and abs(c - d) > abs(c + A[r] - (d - A[r])):
        c += A[r]
        d -= A[r]
        r += 1
    ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
    # 真ん中を動かす
    b += A[m]
    c -= A[m]
    m += 1
    # 真ん中が右に追いついたら、右も合わせて+1する
    if m == r:
        c += A[r]
        d -= A[r]
        r += 1
print(ans)
