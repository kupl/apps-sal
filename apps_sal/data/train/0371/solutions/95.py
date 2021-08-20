class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = [set(j) for j in routes]
        graph = {}
        for (bus, route) in enumerate(routes):
            graph.setdefault(bus, [])
            for other_bus in range(bus + 1, len(routes)):
                if any((r in routes[other_bus] for r in route)):
                    graph[bus].append(other_bus)
                    graph.setdefault(other_bus, [])
                    graph[other_bus].append(bus)
        level = 1
        queue = [i for i in range(len(routes)) if S in routes[i]]
        seen = set()
        for bus in queue:
            seen.add(bus)
        while queue:
            new_queue = []
            for bus in queue:
                if T in routes[bus]:
                    return level
                for neighbor_bus in graph[bus]:
                    if neighbor_bus not in seen:
                        seen.add(neighbor_bus)
                        new_queue.append(neighbor_bus)
            queue = new_queue
            level += 1
        return -1
