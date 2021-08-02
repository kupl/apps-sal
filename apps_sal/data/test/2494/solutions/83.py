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
INF = float('inf')
MOD = 10 ** 9 + 7


def dijkstra(N: int, nodes: list, src: int) -> list:
    """ ダイクストラ高速化版(頂点数, 隣接リスト(0-indexed), 始点) """
    from heapq import heappush, heappop

    res = [INF] * N
    # スタート位置(今回は開始コストが0じゃないので1*Nを含める)
    que = [1 * N + src]
    # 今回の開始位置1のコストは1
    res[src] = 1 * N

    while len(que) != 0:
        cur = heappop(que)
        dist = cur // N
        cur %= N
        for nxt, cost in nodes[cur]:
            if dist + cost < res[nxt]:
                res[nxt] = dist + cost
                heappush(que, (dist + cost) * N + nxt)
    return res


K = INT()

nodes = [[] for i in range(K)]
for i in range(K):
    nodes[i].append(((i + 1) % K, 1))
    nodes[i].append(((i * 10) % K, 0))

res = dijkstra(K, nodes, 1)
print((res[0]))
