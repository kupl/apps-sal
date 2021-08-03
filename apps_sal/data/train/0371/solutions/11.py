from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        route_dict = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                route_dict[stop].add(i)

        queue = deque([S])
        seen = set([S])
        buses = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                stop = queue.popleft()
                if stop == T:
                    return buses
                for i in route_dict[stop]:
                    for j in routes[i]:
                        if j not in seen:
                            queue.append(j)
                            seen.add(j)
                    routes[i] = []
            buses += 1

        return -1
