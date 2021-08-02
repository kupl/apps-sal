from collections import defaultdict, deque
from bisect import bisect
from sys import setrecursionlimit
from threading import stack_size, Thread
MOD = 10 ** 9 + 7


def dfs_order(i, visited, g, order):
    if visited[i]:
        return
    visited[i] = 1
    for j in g[i]:
        dfs_order(j, visited, g, order)
    order.append(i)


def dfs_scc(leader, s, rg, visited, comp, cost):
    if visited[s]:
        return
    visited[s] = 1
    for j in rg[s]:
        dfs_scc(leader, j, rg, visited, comp, cost)
    comp[leader].append(cost[s])


def main():
    n = int(input())
    cost = [0] + [int(i) for i in input().split()]
    m = int(input())
    g = [[] for i in range(n + 1)]
    rg = [[] for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        rg[b].append(a)

    order = deque()
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_order(i, visited, g, order)
    # print(order)

    visited = [0] * (n + 1)
    comp = defaultdict(list)
    while order:
        now = order.pop()
        if not visited[now]:
            dfs_scc(now, now, rg, visited, comp, cost)
    # print(comp)

    ans1, ans2 = 0, 1
    for key, values in comp.items():
        values = sorted(values)
        ans1 += values[0]
        position = bisect(values, values[0])
        ans2 = (ans2 * position + MOD) % MOD
    print(ans1, ans2)


setrecursionlimit(MOD)
stack_size(102400000)
t = Thread(target=main)
t.start()
