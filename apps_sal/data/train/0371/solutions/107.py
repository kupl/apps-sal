class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        graph = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if set(routes[i]) & set(routes[j]): 
                    graph[i].add(j)
                    graph[j].add(i)
        routeSet = [set(route) for route in routes]
        startRoutes = [i for i in range(len(routes)) if S in routeSet[i]]
        q, visited = deque([(i, 1) for i in startRoutes]), set(startRoutes)
        while q:
            r, step = q.popleft()
            if T in routeSet[r]: return step
            for nr in graph[r]:
                if nr not in visited:
                    visited.add(nr)
                    q += (nr, step + 1),
        return -1
