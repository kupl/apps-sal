class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            
            return 0
        
        routes = [set(route) for route in routes]
        
        reachable = collections.defaultdict(list)
        
        for i in range(len(routes)):
            
            for j in range(i + 1, len(routes)):
                
                if any([stop in routes[j] for stop in routes[i]]):
                    
                    reachable[i].append(j)
                    
                    reachable[j].append(i)
        
        target_routes = set()
        
        q = []
        
        visited = set()
        
        for i in range(len(routes)):
            
            if S in routes[i]:
                
                q.append((i, 1))
                
                visited.add(i)
                
            if T in routes[i]:
                
                target_routes.add(i)
                
        while q:
            
            route, count = q.pop(0)
            
            if route in target_routes:
                
                return count
            
            for next_route in reachable[route]:
                
                if next_route not in visited:
                    
                    visited.add(next_route)
                    
                    q.append((next_route, count + 1))
                    
        return -1
