class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
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
        (visited, targets) = (set(), set())
        for (bus, route) in enumerate(routes):
            if S in route:
                visited.add(bus)
            if T in route:
                targets.add(bus)
        queue = []
        for bus in visited:
            queue.append((bus, 1))
        while queue:
            (bus, numBuses) = queue.pop(0)
            if bus in targets:
                return numBuses
            visited.add(bus)
            for connecting_bus in graph[bus]:
                if connecting_bus not in visited:
                    queue.append((connecting_bus, numBuses + 1))
        return -1
