class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        graph = defaultdict(set)
        routes = list(map(set, routes))
        seen = set()
        target = set()
        q = deque()
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i] & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)
            if S in routes[i]:
                q.append((i, 1))
                seen.add(i)
            if T in routes[i]:
                target.add(i)
        while q:
            (cur, count) = q.popleft()
            if cur in target:
                return count
            for rt in graph[cur]:
                if rt not in seen:
                    q.append((rt, count + 1))
                    seen.add(rt)
        return -1
