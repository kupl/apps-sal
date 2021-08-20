import heapq


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = defaultdict(list)
        routes_set = []
        for route in routes:
            routes_set.append(set(route))
        for (i, r1) in enumerate(routes_set):
            for j in range(i + 1, len(routes_set)):
                r2 = routes_set[j]
                if any([r in r2 for r in r1]):
                    graph[i].append(j)
                    graph[j].append(i)
        target = set()
        visited = set()
        for (i, r) in enumerate(routes_set):
            if S in r:
                visited.add(i)
            if T in r:
                target.add(i)
        queue = [(bus, 1) for bus in visited]
        while queue:
            (bus, moves) = queue.pop(0)
            if bus in target:
                return moves
            for nei in graph[bus]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, moves + 1))
        return -1
