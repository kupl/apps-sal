class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for (i, route1) in enumerate(routes):
            for j in range(i + 1, len(routes)):
                route2 = routes[j]
                if route1 & route2:
                    graph[i].add(j)
                    graph[j].add(i)
        seen = set()
        target = set()
        for (bus, route) in enumerate(routes):
            if S in route:
                seen.add(bus)
            if T in route:
                target.add(bus)
        Q = [(1, bus) for bus in seen]
        for (steps, bus) in Q:
            if bus in target:
                return steps
            for nbr in graph[bus]:
                if nbr not in seen:
                    seen.add(nbr)
                    Q.append((steps + 1, nbr))
        return -1
