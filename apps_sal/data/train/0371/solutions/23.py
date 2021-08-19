from collections import deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = {}
        for bus in range(len(routes)):
            route = routes[bus]
            for stop in route:
                if stop in graph:
                    graph[stop].append(bus)
                else:
                    graph[stop] = [bus]
        q = deque()
        q.append((-1, 0))
        taken = set()
        while len(q) > 0:
            busTuple = q.popleft()
            bus = busTuple[0]
            numBusses = busTuple[1]
            if bus != -1 and T in routes[bus]:
                return numBusses
            if bus == -1:
                for nextBus in graph[S]:
                    if nextBus not in taken:
                        taken.add(nextBus)
                        q.append((nextBus, numBusses + 1))
            else:
                for stop in routes[bus]:
                    for nextBus in graph[stop]:
                        if nextBus not in taken:
                            taken.add(nextBus)
                            q.append((nextBus, numBusses + 1))
        return -1
