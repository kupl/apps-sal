class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = dict()
        for i,stops in enumerate(routes):
            for j in stops:
                if j not in graph:
                    graph[j] = set()
                graph[j].add(i)
        
                
                
        
        
        buses = 0
        if S==T:
            return 0
        queue = collections.deque()
        visited  = set()
        
        
        queue.append((S,0))
        visited.add(S)
        
        while len(queue)>0:
            
            curr_stop,depth  = queue.popleft()
            if curr_stop==T:
                return depth



            for stop in graph[curr_stop]:
                for j in routes[stop]:
                    if j not in visited:

                        queue.append((j,depth+1))
                        visited.add(j)
                        
            
            
            
        return -1
                    
        
        
        
                
        
        

