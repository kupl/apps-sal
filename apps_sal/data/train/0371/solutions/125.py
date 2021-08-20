from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(list)
        for (i, route) in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        if S not in graph or T not in graph:
            return -1
        if S == T:
            return 0
        visitedStop = set()
        visitedStop.add(S)
        visitedRoute = set()
        visitedRoute.update(graph[S])
        res = 1
        queue = deque(graph[S])
        while queue:
            for i in range(len(queue)):
                p = queue.pop()
                route = routes[p]
                for n in route:
                    if n == T:
                        return res
                    if n in visitedStop:
                        continue
                    visitedStop.add(n)
                    routeIndex = graph[n]
                    for r in routeIndex:
                        if r in visitedRoute:
                            continue
                        queue.appendleft(r)
                        visitedRoute.add(r)
            res += 1
        return -1
