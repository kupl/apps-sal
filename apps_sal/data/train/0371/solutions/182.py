class Solution: # 368 ms
    def numBusesToDestination(self, routes, start, target):
        if start == target: return 0

        stop2Route = defaultdict(set)
     #   route2Stop = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
              #  route2Stop[i].add(stop)
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
                     #   if target in route2Stop[route]:
                     #       return step
                     #   else:
                            for stop in routes[route]:
                                if stop == target: return step
                                if stop not in visitedStop:
                                    stack.append(stop)
                            visited.add(route)       
            q = stack
         #   print(q, stop, stack, visited, step, visitedStop)
         #   return

        return -1
