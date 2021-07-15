class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        
        graph   = collections.defaultdict(set)
        
        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(bus)
        
        queue   = collections.deque([S])
        visited = set()
        result  = int()
        
        while queue:
            result  += 1
            for _ in range(len(queue)):
                currStop    = queue.popleft()
                for bus in graph[currStop]:
                    if bus not in visited:
                        visited.add(bus)
                        for stop in routes[bus]:
                            if stop == T:
                                return result
                            queue.append(stop)
        return -1
