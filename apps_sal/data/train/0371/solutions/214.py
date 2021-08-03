class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        # traverse bus ROUTES instead of stops
        if S == T:
            return 0
        # build graph of routes
        graph = defaultdict(set)
        routes = list(map(set, routes))
        seen = set()
        target = set()
        q = deque()

        for i in range(len(routes)):
            # for i, r in enumerate(routes):
            # build graph
            for j in range(i + 1, len(routes)):
                if routes[i] & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)
            # add starting routes
            if S in routes[i]:
                q.append((i, 1))
                seen.add(i)
            # add ending routes
            if T in routes[i]:
                target.add(i)

        # traverse from start, return when reaching end
        while q:
            cur, count = q.popleft()
            if cur in target:
                return count
            for rt in graph[cur]:
                if rt not in seen:
                    q.append((rt, count + 1))
                    seen.add(rt)

        return -1
