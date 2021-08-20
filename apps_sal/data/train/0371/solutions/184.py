from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        model as graph
        find shortest path with BFS

        buses connect bus stops

        bus stops are vertices

        no

        routes are connected if they have a common point

        routes are vertices


        """
        if S == T:
            return 0
        g = Graph()
        sets = [set(route) for route in routes]
        for s in sets:
            if S in s and T in s:
                return 1
        for (i, s1) in enumerate(sets):
            for j in range(i + 1, len(sets)):
                s2 = sets[j]
                if not s1.isdisjoint(s2):
                    g.connect(i, j)
        starts = [i for (i, s) in enumerate(sets) if S in s]
        ends = {i for (i, s) in enumerate(sets) if T in s}
        min_steps = [g.min_steps(start, ends) for start in starts]
        return min((x for x in min_steps if x > 0), default=-1)


class Graph:

    def __init__(self):
        self.adj = defaultdict(set)

    def connect(self, p, q):
        self.adj[p].add(q)
        self.adj[q].add(p)

    def min_steps(self, start, ends):
        seen = {start}
        q = deque([start])
        steps = 1
        while q:
            for _ in range(len(q)):
                p = q.popleft()
                if p in ends:
                    return steps
                for v in self.adj[p]:
                    if v in seen:
                        continue
                    seen.add(v)
                    q.append(v)
            steps += 1
        return -1
