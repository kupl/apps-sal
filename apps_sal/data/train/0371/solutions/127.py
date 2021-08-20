class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        to_routes = collections.defaultdict(set)
        for (busId, route) in enumerate(routes):
            for stopId in route:
                to_routes[stopId].add(busId)
        q = collections.deque()
        q.appendleft((S, 0))
        seen = set()
        seen.add(S)
        while q:
            (stopId, busNums) = q.pop()
            if stopId == T:
                return busNums
            for busId in to_routes[stopId]:
                for stop in routes[busId]:
                    if stop not in seen:
                        q.appendleft((stop, busNums + 1))
                        seen.add(stop)
        return -1
