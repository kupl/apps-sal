class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = collections.defaultdict(list)
        if S == T: return 0
        nodeS, nodeT = set(), set()
        for i in range(len(routes)):
            if S in routes[i]: nodeS.add(i)
            if T in routes[i]: nodeT.add(i)
            if i < len(routes) - 1:
                for j in range(1, len(routes)):
                    if set(routes[i]) & set(routes[j]): 
                        graph[i].append(j)
                        graph[j].append(i)
        
        # print(graph)
        if nodeS & nodeT: return 1
        if not nodeS or not nodeT: return -1
                
        queue, visited = collections.deque(), set()
        for s in nodeS:
            queue.append((s, 1))
        
        
        
        while queue:
            # print(queue)
            node, step = queue.popleft()
            if node in nodeT: return step
            for nbr in graph[node]:
                if nbr not in visited:
                    queue.append((nbr, step + 1))
                    visited.add(nbr)
        
        return -1
            
        

