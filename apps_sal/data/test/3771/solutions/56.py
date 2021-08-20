import itertools
import os
import sys
from collections import deque, defaultdict
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
(H, W) = list(map(int, sys.stdin.readline().split()))
table = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
S = H + W
T = H + W + 1
graph = [[] for _ in range(H + W + 2)]
for (h, w) in itertools.product(list(range(H)), list(range(W))):
    if table[h][w] == '.':
        continue
    if table[h][w] == 'S':
        graph[S].append((h, IINF))
        graph[S].append((H + w, IINF))
    elif table[h][w] == 'T':
        graph[h].append((T, IINF))
        graph[H + w].append((T, IINF))
    graph[h].append((H + w, 1))
    graph[H + w].append((h, 1))


class Dinic:

    def __init__(self, graph=None, residual=None):
        """
        :param list of (list of (int, int)) graph: (to, cap) の隣接リスト
        :param list of (list of (list of (int|list))) residual: (to, cap, rev) の残余グラフ
        """
        assert graph and (not residual) or (not graph and residual)
        if graph:
            self.graph = self.residual_graph(graph)
        else:
            self.graph = residual

    @staticmethod
    def residual_graph(graph):
        """
        残余グラフ構築
        :param list of (list of (int, int)) graph: (to, cap) の隣接リスト
        :rtype: list of (list of (list of (int|list)))
        :return: (to, cap, rev) の残余グラフ
        """
        ret = [[] for _ in range(len(graph))]
        for v in range(len(graph)):
            for (u, cap) in graph[v]:
                rev = [v, 0]
                edge = [u, cap, rev]
                rev.append(edge)
                ret[v].append(edge)
                ret[u].append(rev)
        return ret

    def _dist(self, s):
        """
        :param int s:
        :rtype: list of int
        :return: s からの距離。残余グラフ上で到達できない場合は -1
        """
        ret = [-1] * len(self.graph)
        ret[s] = 0
        que = deque([(s, 0)])
        while que:
            (v, d) = que.popleft()
            for (u, cap, _) in self.graph[v]:
                if ret[u] < 0 < cap:
                    ret[u] = d + 1
                    que.append((u, d + 1))
        return ret

    def _dfs(self, s, t, dist, iter, flow=float('inf')):
        """
        :param int s:
        :param int t:
        :param list of int dist:
        :param list of int iter:
        :param int flow:
        """
        if s == t:
            return flow
        while iter[s] < len(self.graph[s]):
            edge = self.graph[s][iter[s]]
            (to, cap, rev) = edge
            if dist[s] < dist[to] and cap > 0:
                f = self._dfs(to, t, dist, iter, min(flow, cap))
                if f > 0:
                    edge[1] -= f
                    rev[1] += f
                    return f
            iter[s] += 1
        return 0

    def maximum_flow(self, from_v, to_v):
        """
        :param int from_v:
        :param int to_v:
        :return: from_v から to_v への最大流
        """
        ret = 0
        while True:
            dist = self._dist(from_v)
            if dist[to_v] < 0:
                break
            iter = [0] * len(self.graph)
            while True:
                flow = self._dfs(from_v, to_v, dist, iter)
                if flow == 0:
                    break
                ret += flow
        return ret


mf = Dinic(graph=graph).maximum_flow(S, T)
if mf >= IINF:
    print(-1)
else:
    print(mf)
