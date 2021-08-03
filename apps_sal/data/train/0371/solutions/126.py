class Solution:
    def numBusesToDestination(self, routes, originStop, destinationStop):
        '''toRoutes = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for j in route:
                toRoutes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T:
                return bus 
            for idx in toRoutes[stop]:
                for nextStop in routes[idx]:
                    if nextStop not in seen:
                        seen.add(nextStop)
                        bfs.append((nextStop, bus+1))
                routes[idx] = []
        return -1'''
        '''Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
        '''
        '''toRoutes = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for r in route:
                toRoutes[r].add(i)
        bfs = [(S,0)]
        seen = set([S])
   
        for stop, bus in bfs:
            if stop == T:
                return bus 
            for idx in toRoutes[stop]:
                for nextStop in routes[idx]:
                    if nextStop not in seen:
                        seen.add(nextStop)
                        bfs.append((nextStop, bus+1))
                #routes[idx] = []
        return -1 '''

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
                        dq.append([nextStop, numOfBuses + 1])
        return -1
