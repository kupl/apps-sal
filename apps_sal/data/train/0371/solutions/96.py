from queue import Queue

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        stopToBus = {}
        for bus in range(len(routes)):
            for stop in routes[bus]:
                stopToBus.setdefault(stop, set())
                stopToBus[stop].add(bus)
        
        q = Queue(maxsize=1000000)
        busVis = [False] * len(routes)
        stopVis = [False] * 1000000
        q.put((S, 0))
        while q.qsize() > 0:
            stop, dist = q.get()
            stopVis[stop] = True
            for bus in stopToBus[stop]:
                if busVis[bus] == False:
                    busVis[bus] = True
                    for ds in routes[bus]:
                        if stopVis[ds] == False:
                            if ds == T:
                                return dist + 1

                            q.put((ds, dist + 1))
        
        return -1
