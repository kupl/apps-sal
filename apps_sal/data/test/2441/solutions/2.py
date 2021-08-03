from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappop, heappush
import bisect
import sys
import threading
mod = 10**9 + 7


def dfs_order(i, visited, G, order):
    if visited[i]:
        return
    visited[i] = 1
    for j in G[i]:
        dfs_order(j, visited, G, order)
    order.append(i)


def dfs_scc(leader, s, RG, visited, comp, cost):
    if visited[s]:
        return
    visited[s] = 1
    for j in RG[s]:
        dfs_scc(leader, j, RG, visited, comp, cost)
    comp[leader].append(cost[s])


def main():
    n = int(input())
    cost = [0] + [int(i) for i in input().split()]
    m = int(input())
    G = [[] for i in range(n + 1)]
    RG = [[] for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        RG[b].append(a)
    order = deque()
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_order(i, visited, G, order)

    visited = [0] * (n + 1)
    comp = defaultdict(list)
    while order:
        now = order.pop()
        if not visited[now]:
            dfs_scc(now, now, RG, visited, comp, cost)

    ans1, ans2 = 0, 1
    for k, v in comp.items():
        v = sorted(v)
        ans1 += v[0]
        poss = bisect.bisect_right(v, v[0])
        ans2 = (ans2 * poss + mod) % mod

    print(ans1, ans2)


def __starting_point():
    sys.setrecursionlimit(200000)
    threading.stack_size(102400000)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
