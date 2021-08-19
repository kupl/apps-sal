class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes_map = {}
        graph = {}
        for i in range(len(routes)):
            routes_map[i] = set()
            for j in range(len(routes[i])):
                routes_map[i].add(routes[i][j])
                if routes[i][j] not in graph:
                    graph[routes[i][j]] = set()
                graph[routes[i][j]].add(i)
        queue = []
        visited = set()
        bus_stop_visited = set()
        for route in routes_map:
            if S in routes_map[route]:
                for bus_stop in routes_map[route]:
                    queue.append((bus_stop, route))
                    bus_stop_visited.add(bus_stop)
                visited.add(route)
        path = 1
        while queue:
            length = len(queue)
            for i in range(len(queue)):
                (bus_stop, route) = queue.pop(0)
                if T in routes_map[route]:
                    return path
                for neighbor_route in graph[bus_stop]:
                    if neighbor_route not in visited:
                        for neighbor_bus_stop in routes_map[neighbor_route]:
                            if neighbor_bus_stop not in bus_stop_visited:
                                bus_stop_visited.add(neighbor_bus_stop)
                                queue.append((neighbor_bus_stop, neighbor_route))
                        visited.add(neighbor_route)
            path += 1
        return -1
