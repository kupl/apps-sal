class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        
        n = len(routes)
        
        graph = defaultdict(set)
        
        for i in range(n):
            for j in range(i+1,n):
                if set(routes[i]).intersection(routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)
                    
        
        # Get source and destination
        for i in range(n):
            if S in routes[i]:
                if T in routes[i]:
                    return 1  
                source = i
            elif T in routes[i]:
                dest = i
                
                
                
        q = deque([[source, 1]])
        visited = [False]*n
        visited[source] = True
        
        while q:
            node, dis = q.popleft()
            if node == dest:
                return dis
            for u in graph[node]:
                if not visited[u]:
                    visited[u] = True
                    q.append([u, dis +1])
                    
        return -1
            
        

