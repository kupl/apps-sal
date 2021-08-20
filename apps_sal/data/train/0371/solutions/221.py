from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        new_routes = {}
        for (i, route) in enumerate(routes):
            new_routes[i] = set(route)
        start_buses = set()
        target_buses = set()
        queue = []
        stop_bus = defaultdict(set)
        for (bus, route) in enumerate(routes):
            for bus2 in range(bus + 1, len(routes)):
                if len(new_routes[bus].intersection(new_routes[bus2])) > 0:
                    stop_bus[bus].add(bus2)
                    stop_bus[bus2].add(bus)
            if S in new_routes[bus]:
                start_buses.add(bus)
                queue.append((bus, 1))
            if T in new_routes[bus]:
                target_buses.add(bus)
        while queue:
            (curr_bus, path) = (queue[0][0], queue[0][1])
            queue = queue[1:]
            if curr_bus in target_buses:
                return path
            for neigh in stop_bus[curr_bus]:
                if neigh not in start_buses:
                    start_buses.add(neigh)
                    queue.append((neigh, path + 1))
        return -1
