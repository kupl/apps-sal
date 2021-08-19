class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)
        for (idx, val) in enumerate(manager):
            tree[val].append(idx)
        self.max_time = 0

        def dfs(node, time):
            new_time = time + informTime[node]
            self.max_time = max(self.max_time, new_time)
            for child in tree[node]:
                dfs(child, new_time)
        dfs(headID, 0)
        return self.max_time
