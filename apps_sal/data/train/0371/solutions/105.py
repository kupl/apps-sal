class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, destination: int) -> int:
        if not routes:
            return -1

        if source == destination:
            return 0

        connections = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                connections[stop].append(i)

        routes = [set(route) for route in routes]

        sources = [[source, route, 1] for route in connections[source]]
        q, visited = collections.deque(sources), set()
        while q:
            stop, route, bus = q.popleft()
            if stop == destination or destination in routes[route]:
                return bus
            visited.add((stop, route))
            for nxt_stop in routes[route]:
                if len(connections[nxt_stop]) == 1:
                    continue
                if (nxt_stop, route) not in visited:
                    q.append((nxt_stop, route, bus))
                    for nxt_route in connections[nxt_stop]:
                        if nxt_route != route:
                            q.append((nxt_stop, nxt_route, bus + 1))
        return -1
