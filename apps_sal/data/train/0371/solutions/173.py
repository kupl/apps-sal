class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop_to_bus = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(bus)

        q = collections.deque([(S, 0)])

        visited = set()
        while q:
            stop, bus = q.popleft()
            visited.add(stop)
            if stop == T:
                return bus

            for next_bus in stop_to_bus[stop]:
                for next_stop in routes[next_bus]:
                    if next_stop not in visited:
                        q.append((next_stop, bus + 1))
                routes[next_bus] = []
        return -1
