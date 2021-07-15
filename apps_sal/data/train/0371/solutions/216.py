class Solution:
    def numBusesToDestination(self, routes: List[List[int]], s: int, t: int) -> int:
        if s == t: return 0
            
        n_buses = len(routes)
        
        stops = defaultdict(lambda: set())
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].add(i)
                
        g = [set() for _ in range(n_buses)]
        for i, route in enumerate(routes):
            for stop in route:
                for bus in stops[stop]:
                    if bus == i: continue
                    g[i].add(bus)
                
        used = [False]*n_buses
        q = collections.deque()
        for bus in stops[s]:
            q.append((bus, 1))
            used[bus] = True
        
        while q:
            bus, dist = q.popleft()
            if bus in stops[t]:
                return dist
            for bus2 in g[bus]:
                if not used[bus2]:
                    q.append((bus2, dist+1))
                    used[bus2] = True
        return -1

