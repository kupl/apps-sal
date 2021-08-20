from collections import defaultdict


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = [set(r) for r in routes]
        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                for k in routes[i]:
                    if k in routes[j]:
                        graph[j].append(i)
                        graph[i].append(j)
                        break
        queue = []
        for (i, poss) in enumerate(routes):
            if S in poss:
                queue.append((i, 1))
        seen = set()
        while queue:
            (cur, cost) = queue.pop(0)
            if T in routes[cur]:
                return cost
            seen.add(cur)
            for child in graph[cur]:
                if child not in seen:
                    queue.append((child, cost + 1))
        return -1
