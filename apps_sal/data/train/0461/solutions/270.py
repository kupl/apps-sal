from collections import defaultdict
from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        eg = defaultdict(set)
        mgr = None
        for i, man in enumerate(manager):
            if man != -1:
                eg[man].add(i)
            else:
                mgr = i
        time_map = {}
        for i, time in enumerate(informTime):
            time_map[i] = time
        q = deque()
        q.append((mgr, time_map[mgr]))
        max_it = -float('inf')

        while q:
            node, dist = q.popleft()
            if len(eg[node]) == 0:
                max_it = max(max_it, dist)

            for neighbor in eg[node]:
                q.append((neighbor, dist + time_map[neighbor]))

        return max_it
