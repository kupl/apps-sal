from collections import deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        def bfs(graph, routes, visited, start_bus, T):
            queue = deque()
            queue.append([start_bus, 1])
            while queue:
                (bus, count) = queue.popleft()
                visited.add(bus)
                if T in routes[bus]:
                    return count
                else:
                    for neighbor in graph[bus]:
                        if neighbor not in visited:
                            queue.append([neighbor, count + 1])
            return float('inf')
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for (i, r1) in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any((r in r2 for r in r1)):
                    graph[i].add(j)
                    graph[j].add(i)
        result = float('inf')
        for bus in range(len(routes)):
            if S in routes[bus]:
                min_path = bfs(graph, routes, set(), bus, T)
                result = min(result, min_path)
        if result == float('inf'):
            return -1
        return result
