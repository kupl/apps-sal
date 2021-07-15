class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        '''
        # BFS
        # Treat each bus stop as node => TLE
        # A node is connected with all nodes in the same route(s)
        # Time: O(V + E)
        # Space: O(V + E)
        
        # Build up adjacency list
        adj = collections.defaultdict(set)
        for route in routes:
            for stop in route:
                adj[stop].update(route)
            
        q = collections.deque()
        q.append(S)
        visited = set()
        visited.add(S)
        buses = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u == T:
                    return buses
                for v in adj[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
            buses += 1
        return -1
        '''
        
        # BFS
        # Treat each bus route as node
        # A node is connected with all routes that share a common bus stop
        
        # Build up adjacency list
        adj = collections.defaultdict(set)
        n = len(routes)
        for i in range(n):
            u = routes[i]
            for j in range(i+1, n):
                v = routes[j]
                if set(u).intersection(set(v)):
                    adj[i].add(j)
                    adj[j].add(i)
                    
        # Build up bus stop -> bus route mapping
        stop2route = collections.defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                stop2route[stop].add(route)

        if S == T:
            return 0
        
        adj[-1] = set([r for r in range(n) if r in stop2route[S]]) # route -1 is connected to all routes that contains S
        q = collections.deque()
        q.append(-1)
        visited = set()
        visited.add(-1)
        buses = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u in stop2route[T]:
                    return buses
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            buses += 1
        return -1

