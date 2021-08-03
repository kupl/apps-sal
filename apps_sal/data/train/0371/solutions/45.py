from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        path = defaultdict(list)
        for i, v in enumerate(routes):
            for bus_stop in v:
                path[bus_stop].append(i)
        used = set()
        queue = deque([S])
        taken = 0
        while queue:
            for _ in range(len(queue)):
                bus_stop = queue.popleft()
                if bus_stop == T:
                    return taken
                for route in path[bus_stop]:
                    if route not in used:
                        used.add(route)
                        for next_bus in routes[route]:
                            if next_bus != bus_stop:
                                queue.append(next_bus)
            taken += 1
        return -1
