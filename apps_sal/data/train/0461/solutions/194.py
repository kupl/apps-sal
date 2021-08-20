from collections import defaultdict, deque


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if not n:
            return 0
        edges = defaultdict(list)
        root = 0
        for (idx, val) in enumerate(manager):
            if val == -1:
                root = idx
            else:
                edges[val].append(idx)
        self.ans = 0
        self.dfs(root, edges, informTime[root], informTime)
        return self.ans

    def dfs(self, node, edges, curr_time, informTime):
        self.ans = max(self.ans, curr_time)
        for reporter in edges[node]:
            self.dfs(reporter, edges, curr_time + informTime[reporter], informTime)
