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
        graph = {bus: set() for bus in range(len(routes))}
        for bus in range(len(routes) - 1):
            for other_bus in range(bus + 1, len(routes)):
                if any((stop in routes[other_bus] for stop in routes[bus])):
                    graph[bus].add(other_bus)
                    graph[other_bus].add(bus)
        result = float('inf')
        for bus in range(len(routes)):
            if S in routes[bus]:
                min_path = bfs(graph, routes, set(), bus, T)
                result = min(result, min_path)
        if result == float('inf'):
            return -1
        return result
