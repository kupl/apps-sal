class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0
        if not routes or not routes[0]:
            return -1

        routesByStop = collections.defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                routesByStop[stop].add(i)

        queue, visited = collections.deque([[0, S]]), {S}

        while queue:
            buses, stop = queue.popleft()
            if stop == T:
                return buses
            for route in routesByStop[stop]:
                for next_stop in routes[route]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append([buses + 1, next_stop])

        return -1
