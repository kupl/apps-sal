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
        visitedStop = set()
        (curr, other) = ({start}, {target})
        step = 0
        while curr and other:
            stack = set()
            step += 1
            while curr:
                stop = curr.pop()
                visitedStop.add(stop)
                for route in stop2Route[stop]:
                    if route in route2Stop:
                        for stop in routes[route]:
                            if stop not in visitedStop:
                                stack.add(stop)
                        del route2Stop[route]
            if stack & other:
                return step
            curr = stack
            if len(curr) > len(other):
                (curr, other) = (other, curr)
        return -1
