from collections import deque


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        visited = set()
        graph = defaultdict(list)
        for (idx, m) in enumerate(manager):
            graph[m].append(idx)
        max_val = 0
        q = deque()
        q.append([headID, 0])
        while len(q):
            (parent, weight) = q.popleft()
            max_val = max(max_val, weight)
            for child in graph[parent]:
                q.append((child, weight + informTime[parent]))
        return max_val
