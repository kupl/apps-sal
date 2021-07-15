class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            return 0
        
        graph = {}
        
        bs = {}
        for i, route in enumerate(routes):
            for s in route:
                if s not in bs:
                    bs[s] = set()
                
                for b in bs[s]:
                    # connect b and i
                    if b not in graph:
                        graph[b] = set()
                    if i not in graph:
                        graph[i] = set()
                    graph[b].add(i)
                    graph[i].add(b)
                
                bs[s].add(i)
        
        if S not in bs:
            return -1
        
        
#         print(\"bs: {}\".format(bs))
#         print(\"graph: {}\".format(graph))
        
        q = collections.deque(list(bs[S]))
        bus_taken = 1
        visited = set(list(bs[S]))
        
        while len(q):
            l = len(q)
            for _ in range(l):
                curt = q.popleft()
                
                if curt in bs[T]:
                    return bus_taken
                
                if curt in graph:
                    for nb in graph[curt]:
                        if nb not in visited:
                            visited.add(nb)
                            q.append(nb)
                
            bus_taken += 1
            
        return -1
