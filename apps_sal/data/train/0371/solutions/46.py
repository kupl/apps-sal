from collections import defaultdict, deque


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        R = defaultdict(list)
        for (idx, r) in enumerate(routes):
            for s in r:
                R[s].append(idx)
        queue = deque([(S, 0)])
        visited = set()
        while queue:
            (cur, res) = queue.popleft()
            if cur == T:
                return res
            for stop in R[cur]:
                if stop not in visited:
                    visited.add(stop)
                    for nxt in routes[stop]:
                        if nxt != cur:
                            queue.append((nxt, res + 1))
        return -1
