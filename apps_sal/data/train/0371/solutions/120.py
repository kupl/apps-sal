class Solution:
    def numBusesToDestination(self, routes, originStop, destinationStop):
        stopToBus = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopToBus[stop].add(bus)
        from collections import deque 
        dq = deque([[originStop, 0]])
        visited = set()
        visited.add(originStop)
        while dq:
            stop, numOfBuses = dq.popleft()
            if stop == destinationStop:
                return numOfBuses 
            for bus in stopToBus[stop]:
                for nextStop in routes[bus]:
                    if nextStop not in visited:
                        visited.add(nextStop)
                        dq.append([nextStop, numOfBuses+1])
        return -1 
                        

