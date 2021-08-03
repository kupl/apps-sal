# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
from itertools import permutations
import sys
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7
def input(): return sys.stdin.readline().rstrip()
def YesNo(b): return bool([print('Yes')] if b else print('No'))
def YESNO(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x) - 1


N, M = map(int, input().split())
w = tuple(map(int, input().split()))
MAX_W = max(w)
lv = [() for _ in range(M)]
for i in range(M):
    l, v = map(int, input().split())
    lv[i] = (l, v)
    if v < MAX_W:
        print(-1)
        return
lv.sort(key=lambda a: (a[1], -a[0]))
L, V = [], []
tmp_l = 0
for l, v in lv:
    if tmp_l < l:
        tmp_l = l
        L.append(l)
        V.append(v)
ans = INF
for tmp_w in permutations(w):
    edge = [[] for _ in range(N)]
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + tmp_w[i]
    for i in range(N - 1):
        for j in range(i + 1, N):
            SUM = S[j + 1] - S[i]
            res = bisect_left(V, SUM)
            if res > 0:
                edge[i].append((j, L[res - 1]))
            else:
                edge[i].append((j, 0))
    dp = [0] * N
    for i in range(N):
        for j, l in edge[i]:
            dp[j] = max(dp[j], dp[i] + l)
    ans = min(ans, dp[-1])
print(ans)
