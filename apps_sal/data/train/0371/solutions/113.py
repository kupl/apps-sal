class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        mapping = dict()  # key is bus stop, val is bus number
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in mapping:
                    mapping[stop] = []
                mapping[stop].append(bus)

        queue = []
        stop_visited = set()
        bus_visited = set()
        queue.append((S, 0))
        while queue:
            current, numBuses = queue.pop(0)
            if current == T:
                return numBuses
            stop_visited.add(current)
            for bus in mapping[current]:
                if bus not in bus_visited:
                    bus_visited.add(bus)
                    for stop in routes[bus]:
                        if stop not in stop_visited:
                            queue.append((stop, numBuses + 1))
        return -1
