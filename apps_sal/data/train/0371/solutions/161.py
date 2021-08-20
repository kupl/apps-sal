class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(set)
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].add(i)
        ans = 0
        queue = collections.deque()
        queue.append(S)
        seen_stop = set([S])
        seen_route = set()
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == T:
                    return ans
                for route in graph[stop]:
                    for new_stop in routes[route]:
                        if new_stop not in seen_stop:
                            queue.append(new_stop)
                            seen_stop.add(new_stop)
                    seen_route.add(route)
            ans += 1
        return -1
