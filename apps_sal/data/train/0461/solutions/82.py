class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)

        for idx, val in enumerate(manager):
            tree[val].append(idx)

        self.max_time = 0

        def dfs(node):
            time = 0
            for child in tree[node]:
                time = max(time, dfs(child))
            return informTime[node] + time

        return dfs(headID)
