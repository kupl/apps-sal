class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = defaultdict(set)
        for i in range(0, len(routes)):
            for j in range(i + 1, len(routes)):
                if any(r in routes[j] for r in routes[i]):
                    graph[i].add(j)
                    graph[j].add(i)

        src = set()
        dest = set()
        for index, route in enumerate(routes):
            if S in route:
                src.add(index)
            if T in route:
                dest.add(index)

        queue = deque()
        for node in src:
            queue.append((node, 1))

        seen = set()
        while queue:
            node, step = queue.popleft()
            if node in dest:
                return step
            for nei in graph[node]:
                if nei not in src:
                    src.add(nei)
                    queue.append((nei, step + 1))
        return -1
