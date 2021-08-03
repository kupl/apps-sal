class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        source = set()
        target = set()
        graph = [[] for _ in range(n)]

        for i in range(n):
            routes[i] = set(routes[i])
            if S in routes[i]:
                source.add(i)
            if T in routes[i]:
                target.add(i)

        if not source or not target:
            return -1
        if source & target:
            return 1

        for u in range(n):
            for v in range(1, n):
                if routes[u] & routes[v]:
                    graph[u].append(v)
                    graph[v].append(u)

        queue = [(source.pop(), 1)]
        seen = [0] * n
        while queue:
            new = []
            for u, cost in queue:
                if u in target:
                    return cost
                seen[u] = 1
                for v in graph[u]:
                    if seen[v]:
                        continue
                    seen[v] = 1
                    new.append((v, cost + 1))
            queue = new
        return -1
