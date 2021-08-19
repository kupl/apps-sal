from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        d = defaultdict(list)
        visited = set()
        for (idx, r) in enumerate(routes):
            for s in r:
                d[s].append(idx)
        queue = deque([(S, 0)])
        while queue:
            (cur, step) = queue.popleft()
            if cur == T:
                return step
            for r in d[cur]:
                if r not in visited:
                    for s in routes[r]:
                        queue.append((s, step + 1))
                    visited.add(r)
        return -1
