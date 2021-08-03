class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = defaultdict(list)
        for i, m in enumerate(manager):
            sub[m].append(i)

        def dfs(i):
            m = 0
            for j in sub[i]:
                m = max(m, dfs(j))
            return m + informTime[i]

        return dfs(headID)
