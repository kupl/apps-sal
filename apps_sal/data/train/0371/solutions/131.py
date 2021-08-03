from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source_stop: int, target_stop: int) -> int:
        if source_stop == target_stop:
            return 0
        routes = [list(set(r)) for r in routes]
        stops = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].append(i)
        q = deque()
        visited_stops = set()
        visited_buses = set()
        q.append((source_stop, 0))
        while q:
            stop_num, bus_num = q.popleft()
            visited_stops.add(stop_num)
            for other_bus in stops[stop_num]:
                if other_bus in visited_buses:
                    continue
                for other_stop in routes[other_bus]:
                    if other_stop == target_stop:
                        return bus_num + 1
                    if other_stop not in visited_stops:
                        visited_stops.add(other_stop)
                        q.append((other_stop, bus_num + 1))
        return -1
