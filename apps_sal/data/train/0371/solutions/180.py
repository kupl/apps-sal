class Solution:

    def numBusesToDestination(self, routes, start, target):
        if start == target:
            return 0
        stop2Route = defaultdict(set)
        route2Stop = defaultdict(set)
        for (i, stops) in enumerate(routes):
            for stop in stops:
                route2Stop[i].add(stop)
                stop2Route[stop].add(i)
        visited = set()
        visitedStop = set()
        q = [start]
        step = 0
        while q:
            stack = []
            step += 1
            while q:
                stop = q.pop()
                for route in stop2Route[stop]:
                    if route not in visited:
                        if target in route2Stop[route]:
                            if stop in route2Stop[route]:
                                return step
                        else:
                            stack.extend(route2Stop[route])
                            visited.add(route)
                visitedStop.add(stop)
            for stop in stack:
                if stop not in visitedStop:
                    q.append(stop)
        return -1
