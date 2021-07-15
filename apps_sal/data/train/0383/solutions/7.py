class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        parent = list(range(n))
        size = [1] * n

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            x, y = find(u), find(v)
            if x != y:
                parent[y] = x
                size[x] += size[y]

        graph = [[v for v, x in enumerate(row) if x and u != v] for u, row in enumerate(graph)]
        infected = [False] * n

        for u in range(n):
            if u in initial:
                infected[u] = True

        for u in range(n):
            if not infected[u]:
                for v in graph[u]:
                    if not infected[v]:
                        union(u, v)

        threat = defaultdict(set)

        for u in range(n): # find infected which threaten uninfected components
            if not infected[u]:
                for v in graph[u]:
                    if infected[v]:
                        threat[find(u)].add(v)

        best = 0
        best_idx = -1

        for v in sorted(initial):   # for each infected
            preventable = set()     # find sum of size of distinct uninfected components threatened by one and only one
            for u in graph[v]:
                if len(threat[find(u)]) == 1:
                    preventable.add(find(u))
            total = 1 + sum(size[u] for u in preventable)
            if total > best:
                best = total
                best_idx = v
        return best_idx

