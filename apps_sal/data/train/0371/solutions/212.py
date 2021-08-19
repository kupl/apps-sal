from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = defaultdict(list)
        for idx, route in enumerate(routes):
            for node in route:
                graph[node].append(idx)
        visited_stop = set([S])
        visited_bus = [0 for _ in range(len(routes))]
        queue = [(idx, 0) for idx in graph[S]]  # bus idx
        # for bus, _ in queue:
        #     visited_bus[bus] = 1
        while queue:
            bus_id, depth = queue.pop(0)
            new_stop = set(routes[bus_id]) - visited_stop
            visited_stop = visited_stop | new_stop
            for stop in new_stop:
                if stop == T:
                    return depth + 1
                for bus in graph[stop]:
                    if visited_bus[bus] == 0:
                        visited_bus[bus] = 1
                        queue.append((bus, depth + 1))
        return -1
