class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S==T:
            return 0
        
        s2b = {}
        for b, route in enumerate(routes):
            for s in route:
                if s not in s2b:
                    s2b[s] = set()
                s2b[s].add(b)
                
        q = collections.deque([S])
        visited = set()
        
        buses = 1
        while len(q):
            l = len(q)
            for _ in range(l):
                curt = q.popleft()
                # if curt in s2b:
                for nb in s2b[curt]:
                    if nb in visited:
                        continue
                    visited.add(nb)
                    for ns in routes[nb]:
                        if ns == T:
                            return buses
                        q.append(ns)
            
            buses += 1
        return -1
