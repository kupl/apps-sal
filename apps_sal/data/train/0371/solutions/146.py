class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(set)
        
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        
        ans = 0
        
        queue = collections.deque([S])
        seen_stop = set()
        seen_route = set()
        
        seen_stop.add(S)
        
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                
                if stop == T:
                    return ans
                
                for routeId in graph[stop]:
                    for new_stop in routes[routeId]:
                        if new_stop not in seen_stop:
                            queue.append(new_stop)
                            seen_stop.add(new_stop)
                
            ans += 1
        
        return -1

