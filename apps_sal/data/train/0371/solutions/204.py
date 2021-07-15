class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            return 0
        
        neighbors = collections.defaultdict(set)
        
        for j, route in enumerate(routes):
            for i in route:
                neighbors[i].add(j)
                
        stack = []
        stack.append((S, 0))
        visited = set()
        visited.add(S)
        visited_route = set()
        
        for stop, count in stack:
            if stop == T:
                return count

            for neighbor in neighbors[stop]:
                if neighbor not in visited_route:
                    for bus in routes[neighbor]:
                        if bus != stop and bus not in visited:
                            stack.append((bus, count + 1))
                            visited.add(bus)
                        
                #routes[neighbor] = []
                visited_route.add(neighbor)
                
        return  -1
            
        

