from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S==T: return 0
        bus2stops = defaultdict(list)
        stop2buses = defaultdict(list)
        for bus,stops in enumerate(routes):
            for stop in stops:
                bus2stops[bus].append(stop)
                stop2buses[stop].append(bus)
        
        q = deque()
        visitedBuses = set()
        for bus in stop2buses[S]:
            q.extend(bus2stops[bus])
            visitedBuses.add(bus)
        visitedStops = set(q)
        if T in visitedStops: return 1
        
        numBuses = 2
        while q:
            for _ in range(len(q)):
                currStop = q.popleft()

                for bus in stop2buses[currStop]:
                    if bus in visitedBuses: 
                        continue
                    visitedBuses.add(bus)
                    for stop in bus2stops[bus]:
                        if stop not in visitedStops:
                            if stop==T:
                                return numBuses
                            visitedStops.add(stop)
                            q.append(stop)
            numBuses+=1
        return -1
