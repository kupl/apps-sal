from collections import defaultdict, deque
from itertools import permutations


class Graph:
    def __init__(self):
        self.E = {}
        self.V = defaultdict(list)

    def put(self, v1, v2):
        if v1 not in self.E:
            self.E[v1] = 1
        if v2 not in self.E:
            self.E[v2] = 1
        self.V[v1].append(v2)
        self.V[v2].append(v1)

    def _adj(self, v1):
        return self.V[v1]

    def bfs(self, v):
        visited = set([v])
        path = [v]
        q = deque([v])
        while q:
            v1 = q.pop()
            for v2 in self._adj(v1):
                if v2 not in visited:
                    visited.add(v2)
                    path.append(v2)
                    q.appendleft(v2)

        return path


def __starting_point():
    n = int(input())
    cp = []
    for _ in range(3):
        cp.append(list(map(int, input().split(' '))))

    inv = False
    vert = defaultdict(int)
    graph = Graph()
    for _ in range(n - 1):
        v1, v2 = list(map(int, input().split(' ')))
        vert[v1] += 1
        if vert[v1] > 2:
            inv = True
            break
        vert[v2] += 1
        if vert[v2] > 2:
            inv = True
            break

        graph.put(v1, v2)

    if inv:
        print(-1)
    else:
        for key in vert:
            if vert[key] == 1:
                start = key
                break

        path = graph.bfs(start)

        min_cost = float('inf')
        min_cost_perm = (0, 1, 2)
        for p in permutations([0, 1, 2]):
            cur_cost = 0
            for i, v in enumerate(path):
                cur_cost += cp[p[i % 3]][v - 1]

            if cur_cost < min_cost:
                min_cost_perm = p
                min_cost = cur_cost

        ans = [0] * n
        for i, v in enumerate(path):
            ans[v - 1] = min_cost_perm[i % 3] + 1

        print(min_cost)
        print(' '.join(map(str, ans)))


__starting_point()
