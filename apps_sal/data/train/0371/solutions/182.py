class Solution:
    def numBusesToDestination(self, routes, start, target):
        if start == target:
            return 0

        stop2Route = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stop2Route[stop].add(i)

        visited = set()
        visitedStop = set()

        q = [start]
        step = 0
        while q:
            stack = []
            step += 1
            for stop in q:
                visitedStop.add(stop)
                for route in stop2Route[stop]:
                    if route not in visited:
                        for stop in routes[route]:
                            if stop == target:
                                return step
                            if stop not in visitedStop:
                                stack.append(stop)
                        visited.add(route)
            q = stack

        return -1
