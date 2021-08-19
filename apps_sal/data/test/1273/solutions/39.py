import math
from collections import defaultdict
from heapq import heappop, heappush
import sys
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = 1 << 50
EPS = 1e-08
mod = 10 ** 9 + 7


def mapline(t=int):
    return list(map(t, sysread().split()))


def mapread(t=int):
    return list(map(t, read().split()))


def dfs(c, to, cols, max_counts, pre_col=0):
    colors = set()
    colors.add(pre_col)
    num = 1
    for (idx, n) in to[c]:
        if cols[idx]:
            continue
        for i in range(num, max_counts + 1):
            if not i in colors:
                num = i
                cols[idx] = i
                colors.add(i)
                dfs(n, to, cols, max_counts, i)
                break


def run():
    N = int(sysread())
    to = [[] for _ in range(N + 1)]
    cols = [0] * (N - 1)
    counts = [0 for i in range(N + 1)]
    for i in range(N - 1):
        (a, b) = mapline()
        to[a].append((i, b))
        to[b].append((i, a))
        counts[a] += 1
        counts[b] += 1
    max_counts = max(counts)
    print(max_counts)
    dfs(1, to, cols, max_counts)
    for c in cols:
        print(c)


def __starting_point():
    run()


__starting_point()
