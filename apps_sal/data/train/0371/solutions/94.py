class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        N = len(routes)
        graph = dict()
        for i in range(N):
            routes[i] = set(routes[i])
        for i in range(N):
            if i not in graph:
                graph[i] = set()
            for j in range(i + 1, N):
                if j not in graph:
                    graph[j] = set()
                if i != j:
                    if any((node in routes[i] for node in routes[j])):
                        graph[i].add(j)
                        graph[j].add(i)
        s = set()
        t = set()
        for (i, route) in enumerate(routes):
            if S in route:
                s.add(i)
            if T in route:
                t.add(i)
        if any((node in s for node in t)):
            return 1
        queue = [[i, 1] for i in s]
        visited = s
        for (node, d) in queue:
            for nxt in graph[node]:
                if nxt not in visited:
                    if nxt in t:
                        return d + 1
                    visited.add(nxt)
                    queue.append([nxt, d + 1])
        return -1
