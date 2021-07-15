class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)
        
        visited = set()
        queue = deque()
        queue.append(S)
        
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == T:
                    return level
                
                for bus in graph[curr]:
                    if bus not in visited:
                        for stop in routes[bus]:
                            queue.append(stop)
                    visited.add(bus)
            
            level += 1
        
        return -1
