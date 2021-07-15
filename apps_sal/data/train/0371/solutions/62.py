class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        def bfs():
            Q = []
            seen = set()
            for b in busAtStops[S]:
                Q.append((b, 1))
            
            while Q:
                bus, depth = Q.pop(0)
                if T in routes[bus]:
                    return depth

                for stop in routes[bus]:
                    for bus in busAtStops[stop]:
                        if bus not in seen:
                            seen.add(bus)
                            Q.append((bus, depth+1))
            return -1            
        
        busAtStops = defaultdict(list)
        for i, r in enumerate(routes):
            for stop in r:
                busAtStops[stop].append(i)
            routes[i] = set(routes[i])
        
        return bfs()
                
        

