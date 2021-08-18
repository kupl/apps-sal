class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if set(routes[i]) & set(routes[j]):
                    graph[tuple(routes[i])].append(tuple(routes[j]))
                    graph[tuple(routes[j])].append(tuple(routes[i]))

        min_buses = float('inf')
        for route in graph:
            visited = set()
            if S in route:
                queue = collections.deque([(route, 1)])
                visited.add(route)
                while queue:
                    route, num_buses = queue.popleft()
                    if T in route:
                        min_buses = min(min_buses, num_buses)
                        break
                    for nei in graph[route]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append((nei, num_buses + 1))

        return min_buses if min_buses != float('inf') else -1
