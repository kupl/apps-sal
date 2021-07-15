class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            return 0
        
        graph = self.createGraph(routes)
        # print(g/raph)
        
        sourceBuses = self.getBuses(routes, S)
        targetBuses = set(self.getBuses(routes, T))
        
        # print(sourceBuses, targetBuses)
        if not sourceBuses or not targetBuses:
            return -1
        
        
        
        
        queue = [sourceBuses]
        visited = set(sourceBuses)
        buses = 1
        while queue:
            curLevel = queue.pop()
            newLevel = []
            
            # print(curLevel)
            for station in curLevel:
                if station in targetBuses:
                    return buses
                
                # print(graph[station], visited)
                for conn in graph[station]:
                    if conn not in visited:
                    
                        visited.add(conn)
                        newLevel.append(conn)
            
            # print(newLevel)
            if newLevel:
                queue.append(newLevel)
                buses += 1
        
        return -1
    
    
    def getBuses(self, routes, station):
        buses = []
        for i in range(len(routes)):
            if station in set(routes[i]):
                buses.append(i)
        
        return buses
        
    def createGraph(self, routes):
        graph = defaultdict(set)
        
        for i,route in enumerate(routes):
            routes[i] = set(route)
        
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                if len(routes[i].intersection(routes[j])) > 0:
                    graph[i].add(j)
                    graph[j].add(i)
        
        return graph
