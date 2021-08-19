import sys
import bisect
import math
import itertools
import heapq
import collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        Parameters
        ----------
        u:int
            from node
        v:int
            to node
        d:int
            cost
        directed:bool
            there is direction
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        """
        Parameters
        ----------
        u:int
            from node
        v:int
            to node
        """
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        Parameters
        ----------
        s:int
            start node

        Return
        ----------
        d:dict(int:int)
            shortest cost from start node to each node 
            {to : cost}

        prev:dict(int:int)
            previous node on the shortest path
            {from : to}
        """
        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))  # (cost, 探索候補ノード)
        v = collections.defaultdict(bool)  # 確定済かどうか
        while len(q):
            # ノードuにおけるコストはk
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:  # cost is ud from u to uv
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev


n, m = inpl()
graph = Dijkstra()
for i in range(m):
    u, v = inpl()
    graph.add(u, v + n, 1, directed=True)
    graph.add(u + n, v + n + n, 1, directed=True)
    graph.add(u + n + n, v, 1, directed=True)
s, t = inpl()
ans = 0
d, _ = graph.Dijkstra_search(s)
ans = d[t] if d[t] != INF else - 1
# print(d)
print(ans // 3)
