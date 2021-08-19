
import marshal
from collections import deque
import sys
input = sys.stdin.readline


class Graph:
    def __init__(self, n, directed=False, decrement=True, destroy=False, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [set() for _ in range(self.n)]
        self.parent = [-1] * self.n
        self.info = [-1] * self.n
        for x, y in edges:
            self.add_edge(x, y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        if self.directed == False:
            self.edges[y].add(x)

    def add_adjacent_list(self, i, adjacent_list):
        if self.decrement:
            self.edges[i] = set(map(lambda x: x - 1, adjacent_list))
        else:
            self.edges[i] = set(adjacent_list)

    def bfs(self, start=1, goal=-1, time=0, save=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: （ループがあっても）最短距離。存在しなければ -1
        """
        if self.decrement:
            start -= 1
            goal -= 1
        if not save:
            self.parent = [-1] * self.n
        p, t = start, time
        self.parent[p] = -2
        next_set = deque([(p, t)])

        while next_set:
            p, t = next_set.popleft()
            for q in self.edges[p]:
                if self.parent[q] != -1:
                    continue
                if q == goal:
                    return t + 1
                self.parent[q] = p
                next_set.append((q, t + 1))
        return -1

    def connection_counter(self):
        """
        :return: 連結成分の個数。有効グラフではあまり意味がない。
        """
        cnt = 0
        self.parent = [-1] * self.n
        for start in range(self.n):
            if self.parent[start] == -1:
                cnt += 1
                self.bfs(start + self.decrement, save=True)
        return cnt

    def distance_list(self, start=1, save=False):
        """
        :param start: スタート地点
        :return: スタート地点から各点への距離のリスト
        """
        dist = [-1] * self.n
        if self.decrement:
            start -= 1
        if not save:
            self.parent = [-1] * self.n
        p, t = start, 0
        self.parent[p] = -2
        dist[p] = 0
        next_set = deque([(p, t)])

        while next_set:
            p, t = next_set.popleft()
            for q in self.edges[p]:
                if self.parent[q] != -1:
                    continue
                dist[q] = t + 1
                self.parent[q] = p
                next_set.append((q, t + 1))
        return dist

##################################################################################################


N, M = map(int, input().split())
graph = Graph(N, directed=False, decrement=True, destroy=False)
for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

if -1 in graph.distance_list():
    print("No")
else:
    print("Yes")
    print(*list(p + 1 for p in graph.parent[1:]), sep="\n")
