from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = [set(route) for route in routes]
        graph = collections.defaultdict(set)
        for (i, r1) in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any((r in r2 for r in r1)):
                    graph[i].add(j)
                    graph[j].add(i)
        seen = set()
        target = set()
        for (node, route) in enumerate(routes):
            if S in route:
                seen.add(node)
            if T in route:
                target.add(node)
        q = deque()
        for node in seen:
            q.append((node, 1))
        while q:
            (curr, depth) = q.popleft()
            if curr in target:
                return depth
            for child in graph[curr]:
                if child not in seen:
                    seen.add(child)
                    q.append((child, depth + 1))
        return -1
