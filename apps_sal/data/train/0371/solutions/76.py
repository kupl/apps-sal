from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_to_bus_map = defaultdict(list)
        L = len(routes)
        for i in range(L):
            for stop in routes[i]:
                stop_to_bus_map[stop].append(i)
        route_graph = defaultdict(set)
        for stop in stop_to_bus_map:
            for r1 in stop_to_bus_map[stop]:
                for r2 in stop_to_bus_map[stop]:
                    if r1 != r2:
                        route_graph[r1].add(r2)
        start = set(stop_to_bus_map[S])
        end = set(stop_to_bus_map[T])
        count = 1
        visited = set()
        while len(start) != 0:
            new_start = set()
            for route in start:
                if route in end:
                    return count
                if route in visited:
                    continue
                new_start |= route_graph[route]
            visited |= start
            start = new_start
            count += 1
        return -1
