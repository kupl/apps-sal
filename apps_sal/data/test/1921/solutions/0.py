import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict
import heapq as hq
import math


def dijkstra(G, s):
    n = len(G)
    visited = [False] * n
    weights = [math.inf] * n
    path = [None] * n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        (g, u) = hq.heappop(queue)
        visited[u] = True
        for (v, w) in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return (path, weights)


def solve(grid, sx, sy, ex, ey):
    console('----- solving ------')
    minres = abs(sx - ex) + abs(sy - ey)
    console(minres)
    if grid == []:
        return minres
    d = defaultdict(list)
    grid = [(i, x, y) for (i, (x, y)) in enumerate(grid)]
    grid = sorted(grid, key=lambda x: x[1])
    for ((i1, x1, y1), (i2, x2, y2)) in zip(grid, grid[1:]):
        d[i1].append((i2, x2 - x1))
        d[i2].append((i1, x2 - x1))
    grid = sorted(grid, key=lambda x: x[2])
    for ((i1, x1, y1), (i2, x2, y2)) in zip(grid, grid[1:]):
        d[i1].append((i2, y2 - y1))
        d[i2].append((i1, y2 - y1))
    for (i, x, y) in grid:
        d[-2].append((i, abs(x - sx)))
        d[-2].append((i, abs(y - sy)))
        d[i].append((-1, abs(x - ex) + abs(y - ey)))
    d[-1] = []
    console(list(d.keys()))
    idxs = {k: i for (i, k) in enumerate(d.keys())}
    G = [[] for _ in range(len(idxs))]
    for (e, vrr) in list(d.items()):
        for (v, cost) in vrr:
            G[idxs[e]].append((idxs[v], cost))
    (_, costs) = dijkstra(G, idxs[-2])
    res = costs[idxs[-1]]
    return min(minres, res)


def console(*args):
    return


inp = sys.stdin.readlines()
for case_num in [1]:
    (_, nrows) = list(map(int, inp[0].split()))
    (sx, sy, ex, ey) = list(map(int, inp[1].split()))
    currow = 2
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int, inp[currow].split())))
        currow += 1
    res = solve(grid, sx, sy, ex, ey)
    print(res)
