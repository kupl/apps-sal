class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        station_has_bus = collections.defaultdict(set)
        queue = collections.deque()
        for (bus_id, route) in enumerate(routes):
            for station in route:
                station_has_bus[station].add(bus_id)
        visited = set([S])
        queue.append((S, 0))
        while queue:
            (station, step) = queue.popleft()
            if station == T:
                return step
            for bus_id in station_has_bus[station]:
                for s in routes[bus_id]:
                    if s not in visited:
                        queue.append((s, step + 1))
                        visited.add(s)
        return -1
