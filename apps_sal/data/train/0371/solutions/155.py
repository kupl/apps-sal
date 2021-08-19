class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = collections.defaultdict(set)
        for (i, route) in enumerate(routes):
            for j in route:
                graph[j].add(i)
        queue = collections.deque([(S, 0)])
        seen = set([S])
        while queue:
            (curr, step) = queue.popleft()
            if curr == T:
                return step
            for i in graph[curr]:
                for route in routes[i]:
                    if route not in seen:
                        queue.append((route, step + 1))
                        seen.add(route)
        return -1
