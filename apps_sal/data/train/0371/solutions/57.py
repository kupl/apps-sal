class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = collections.defaultdict(set)  # node is the bus, not stop
        routes = list(map(set, routes))
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        visited, targets = set(), set()
        for i, r in enumerate(routes):
            if S in r:
                visited.add(i)
            if T in r:
                targets.add(i)

        queue = collections.deque([(node, 1) for node in visited])
        while queue:
            node, step = queue.popleft()
            if node in targets:
                return step
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, step + 1))
        return -1
