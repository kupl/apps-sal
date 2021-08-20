import os
import sys
from collections import deque
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
(N, M) = list(map(int, sys.stdin.readline().split()))
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for (a, b) in AB:
    graph[a].append(b)


def cycle_size(from_v):
    """
    from_v に戻ってくるまでのステップ数
    :param from_v:
    :return:
    """
    parents = [None] * len(graph)
    seen = [False] * len(graph)
    que = deque([(from_v, 0)])
    while que:
        (v, d) = que.pop()
        for u in graph[v]:
            if seen[u]:
                continue
            seen[u] = True
            que.appendleft((u, d + 1))
            parents[u] = v
            if u == from_v:
                return (d + 1, parents)
    return (INF, parents)


min_v = None
min_size = INF
min_parents = None
for v in range(1, N + 1):
    (size, parents) = cycle_size(v)
    if size < min_size:
        min_v = v
        min_size = size
        min_parents = parents
if min_size < INF:
    print(min_size)
    print(min_v)
    v = min_parents[min_v]
    while v != min_v:
        print(v)
        v = min_parents[v]
else:
    print(-1)
