        
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T :
           return 0 
        stopToBusDict = defaultdict()
        
        for bus in range(len(routes)):
            for stop in routes[bus]:
                if stop not in stopToBusDict:
                   stopToBusDict[stop] = [] 
                stopToBusDict[stop].append(bus)
    
        routes = [set(r) for r in routes]
        
        adjList = collections.defaultdict(set)
    
        
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    adjList[i].add(j)
                    adjList[j].add(i)    
              
        targets = set()
        visited = set()
        for node, route in enumerate(routes):
            #print(\"T: %s node: %s route: %s\" %(T,node,route))
            if T in route: targets.add(node)
            if S in route: visited.add(node)    
       
            
            
        def bfs(S,T) :
            queue = collections.deque()
            #print(\"target: %s\" %(targets))
            for bus in stopToBusDict[S]:
                queue.append([bus,1])
            while len(queue) != 0 :
                
                currentBus = queue.popleft()
                visited.add(currentBus[0]) 
                
                if currentBus[0] in targets:
                   return currentBus[1]
                
                for neighbour in adjList[currentBus[0]] :
                    if neighbour not in visited :
                       queue.append([neighbour,currentBus[1]+1])
            print(-1)        
            return -1        
                    
                
            
                
                
            
             
            
            
            
            
        return bfs(S,T)      
