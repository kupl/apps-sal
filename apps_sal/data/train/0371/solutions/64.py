class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        stop_to_route = defaultdict(list)

        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_route[stop].append(i)

        graph = {}

        for u in range(len(routes)):
            graph[u] = set()

        for i in range(len(routes)):
            for stop in routes[i]:
                for r2 in stop_to_route[stop]:
                    if r2 != i:
                        graph[i].add(r2)

        end = set(stop_to_route[T])
        visited = [False] * len(routes)

        initial = []

        for r in stop_to_route[S]:
            initial.append((r,1))

        q = deque(initial)

        while q:
            u,cost = q.popleft()

            if u in end:
                return cost

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append((v,cost+1))

        return -1

