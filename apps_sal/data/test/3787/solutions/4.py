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

N, A, B = MAP()

if A * B < N:
    print((-1))
    return
if A + B > N+1:
    print((-1))
    return
if A == 1 and B != N or B == 1 and A != N:
    print((-1))
    return
remain = N - A
if remain < B - 1:
    print((-1))
    return
d, m = divmod(remain, B-1) if B > 1 else (0, 0)
if d > A:
    print((-1))
    return
li = [[] for i in range(B)]
li[0] = list(range(1, A+1))
j = A + 1
for i in range(1, B):
    tmp = []
    for _ in range(d):
        tmp.append(j)
        j += 1
    if m > 0:
        tmp.append(j)
        j += 1
        m -= 1
    li[i] = tmp
li = li[::-1]
ans = []
for grp in li:
    ans += grp
print((*ans))

