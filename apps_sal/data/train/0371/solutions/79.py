class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S==T:
            return 0
        
        graph = collections.defaultdict(list)
        bfs = []
        end = []
        
        for i in range(len(routes)):
            
            if S in routes[i]:
                bfs.append((i,1))
            if T in routes[i]:
                end.append(i)
                
            for j in range(i+1,len(routes)):
                
                if set(routes[i]) & set(routes[j]):
                    
                    graph[i].append(j)
                    graph[j].append(i)
                    
        
        bfs = deque(bfs)
        visited = set(bfs)
        
        while bfs:
            
            ele = bfs.popleft()
            
            bus, nbus = ele
            
            if bus in end:
                return nbus
            
            for edge in graph[bus]:
                if edge not in visited:
                    visited.add(edge)
                    bfs.append((edge,nbus+1))
                    
        return -1
