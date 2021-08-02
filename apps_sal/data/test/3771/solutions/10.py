# ARC074 F #Ford-Fulkerson
# with explanation
from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7

H, W = list(map(int, input().split()))
A = [0] * H
for i in range(H):
    A[i] = str(input())
# print(A)
N = H + W + 2
B = [0] * N
Start = 0
Goal = N - 1
ans = 0
lines = defaultdict(set)
cost = [[0] * (N) for i in range(N)]
for i in range(H):  # i + 1
    for j in range(W):  # H + 1 + j
        if A[i][j] == "S":
            sx, sy = i, j
            lines[0].add(i + 1)
            cost[0][i + 1] = INF
            lines[0].add(H + 1 + j)
            cost[0][H + 1 + j] = INF
        elif A[i][j] == "T":
            gx, gy = i, j
            lines[i + 1].add(N - 1)
            cost[i + 1][N - 1] = INF
            lines[H + 1 + j].add(N - 1)
            cost[H + 1 + j][N - 1] = INF
        elif A[i][j] == "o":
            lines[i + 1].add(H + 1 + j)
            cost[i + 1][H + 1 + j] = 1
            lines[H + 1 + j].add(i + 1)
            cost[H + 1 + j][i + 1] = 1

if sx == gx or sy == gy:
    print((-1))
    return
# print(B)
# print(lines)


def Ford_Fulkerson(s):  # sからFord-Fulkerson
    nonlocal lines
    nonlocal cost
    nonlocal ans
    queue = deque()  # BFS用のdeque
    queue.append([s, INF])
    ed = [True] * (N)  # 到達済み
    ed[s] = False
    route = [0 for i in range(N)]  # ルート
    route[s] = -1
    # BFS
    while queue:
        s, flow = queue.pop()
        for t in lines[s]:  # s->t
            if ed[t]:
                flow = min(cost[s][t], flow)  # flow = min(直前のflow,line容量)
                route[t] = s
                queue.append([t, flow])
                ed[t] = False
                if t == Goal:  # ゴール到達
                    ans += flow
                    break
        else:
            continue
        break
    else:
        return False
    # ラインの更新
    t = Goal
    s = route[t]
    while s != -1:
        # s->tのコスト減少，ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)
        # t->s(逆順)のコスト増加，元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow
        t = s
        s = route[t]

    return True


while True:
    if Ford_Fulkerson(Start):
        continue
    else:
        break

print(ans)
