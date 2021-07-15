class Solution:
    def numBusesToDestination(self, routes, start, target):
        if start == target: return 0
        stop2Route = defaultdict(set)
        route2Stop = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                route2Stop[i].add(stop)
                stop2Route[stop].add(i)

     #   return stop2Route, route2Stop
        visited = set() 
        visitedStop = set()       
        stack = []
        q = [start]
        step = 0
        while q:
            step += 1
            while q:
                stop = q.pop()
                for route in stop2Route[stop]:
                    if route not in visited:
                        if target in route2Stop[route]:
                            # in the same route
                            if stop in route2Stop[route]:
                                return step
                        else:
                            stack.append(route)
                            
                            visited.add(route)
                            
                visitedStop.add(stop) 
                
            for route in stack:
                for stop in route2Stop[route]:
                    if stop not in visitedStop:
                        q.append(stop)
         #   print(q, stop, stack, visited, step, visitedStop)
         #   return

        return -1
