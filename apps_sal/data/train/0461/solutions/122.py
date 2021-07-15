class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node):
            return max([dfs(j) for j in tree[node]] or [0]) + informTime[node]
        ret=[0]
        tree = defaultdict(set)
        for i, m in enumerate(manager):
            tree[m].add(i)
        return dfs(headID)
