class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            return 0
        
        routes = [set(route) for route in routes]
        graph = defaultdict(set)
        
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)
        
        visited = set()
        target = set()
        for node, route in enumerate(routes):
            if S in route:
                visited.add(node)
            
            if T in route:
                target.add(node)
        
        q = deque([(node, 1) for node in visited])
        while q:
            node, transfer = q.popleft()
            if node in target:
                return transfer
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, transfer + 1))
        
        return -1
