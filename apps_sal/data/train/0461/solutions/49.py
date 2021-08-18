class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        M = [[] for m in range(n)]
        for i, m in enumerate(manager):
            if m == -1:
                continue
            M[m].append(i)

        def dfs(id, t):
            t_after_informed = t + informTime[id]
            return max(dfs(sub_id, t_after_informed) for sub_id in M[id]) if M[id] else t_after_informed

        return dfs(headID, 0)
