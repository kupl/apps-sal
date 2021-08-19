class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = collections.defaultdict(set)
        num_buses = len(routes)
        routes = list(map(set, routes))
        for (i, route1) in enumerate(routes):
            for j in range(i + 1, num_buses):
                route2 = routes[j]
                if any((r in route2 for r in route1)):
                    graph[i].add(j)
                    graph[j].add(i)
        (seen, targets) = (set(), set())
        for (node, route) in enumerate(routes):
            if S in route:
                seen.add(node)
            if T in route:
                targets.add(node)
        queue = [(node, 1) for node in seen]
        for (node, depth) in queue:
            if node in targets:
                return depth
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, depth + 1))
        return -1
