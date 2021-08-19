import sys
from collections import deque

input = sys.stdin.readline


class Bellman_Ford:
    def __init__(self, v=None, e=None, lis=None, start=None, end=None, inf=float('inf')):
        self.V = v
        self.E = e
        self.lis = lis
        self.start = start if start else 0
        self.end = end if end else self.V - 1
        self.inf = inf
        self.close_minus = False

    def getlist(self, lis):
        self.lis = lis

    def def_start(self, s):
        self.start = s

    def def_end(self, e):
        self.end = e

    def def_inf(self, inf):
        self.inf = inf

    def def_vertice(self, v):
        self.V = v

    def def_edge(self, e):
        self.E = e

    def prepare(self):
        self.cost = [self.inf] * self.V  # 各頂点への最小コスト
        self.cost[self.start] = 0  # 自身への距離は0

    def search(self):
        for i in range(self.V):
            update = False  # 更新が行われたか
            for x, y, z in self.lis:
                if self.cost[y] > self.cost[x] + z:
                    self.cost[y] = self.cost[x] + z
                    update = True
            if not update:
                break
            # 負閉路が存在
            if i == self.V - 1:
                self.close_minus = True
                return False
        return True

    def main(self):
        self.prepare()
        self.search()

    def cost_all(self):
        return self.cost


def main():
    n, m, p = map(int, input().split())

    graph = [None] * m
    tree_forth = [[] for _ in range(n)]
    tree_back = [[] for _ in range(n)]

    for i in range(m):
        a, b, c = map(int, input().split())
        tree_forth[a - 1].append(b - 1)
        tree_back[b - 1].append(a - 1)
        c = p - c
        graph[i] = (a - 1, b - 1, c)

    already1, already2 = [True] * n, [True] * n
    for already, tree, start in zip([already1, already2], [tree_forth, tree_back], [0, n - 1]):
        not_yet = deque([start])
        already[start] = False
        while not_yet:
            key = not_yet.pop()
            for v in tree[key]:
                if already[v] == False:
                    continue
                already[v] = False
                not_yet.append(v)

    graph_new = []
    for i in range(m):
        a, b, c = graph[i]
        if already1[a] or already1[b] or already2[a] or already2[b]:
            continue
        graph_new.append((a, b, c))

    bf = Bellman_Ford(v=n, e=m, lis=graph_new)
    bf.main()
    if bf.close_minus:
        print(-1)
    else:
        print(max(0, -bf.cost[n - 1]))


def __starting_point():
    main()


__starting_point()
