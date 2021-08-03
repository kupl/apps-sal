from collections import defaultdict, deque


class Solution:
    def bfs(self, start_bus):
        distance = [None] * self.num_buses
        distance[start_bus] = 1
        q = deque([start_bus])
        while q:
            bus = q.popleft()
            if self.target in self.buses_to_stations[bus]:
                return distance[bus]

            for station in self.buses_to_stations[bus]:
                for neighbour_bus in self.stations_to_busses[station]:
                    if distance[neighbour_bus] is None:
                        distance[neighbour_bus] = distance[bus] + 1
                        q.append(neighbour_bus)
        return 2**32

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        self.num_buses = len(routes)
        self.buses_to_stations = [set(route) for route in routes]

        self.stations_to_busses = defaultdict(list)
        self.target = T

        for bus in range(len(routes)):
            for station in routes[bus]:
                self.stations_to_busses[station].append(bus)

        m = 2**32

        for bus in self.stations_to_busses[S]:
            dist_by_bus = self.bfs(bus)
            m = min(m, dist_by_bus)

        if m == 2**32:
            return -1
        else:
            return m
