from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        toRoutes = defaultdict(set)
        for (i, route) in enumerate(routes):
            for j in route:
                toRoutes[j].add(i)
        (queue, visited) = ([(S, 0)], set([S]))
        for (stop, bus) in queue:
            if stop == T:
                return bus
            for i in toRoutes[stop]:
                for j in routes[i]:
                    if j not in visited:
                        visited.add(j)
                        queue.append((j, bus + 1))
        return -1
