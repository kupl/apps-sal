from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = defaultdict(set)

        for bus, route in enumerate(routes):
            for r in route:
                graph[r].add(bus)

        queue = deque([(S, 0)])
        seen = set([S])

        while queue:
            stop, busCnt = queue.popleft()
            if stop == T:
                return busCnt
            for bus in graph[stop]:
                for stp in routes[bus]:
                    if stp not in seen:
                        queue.append((stp, busCnt + 1))
                        seen.add(stp)
        return -1
