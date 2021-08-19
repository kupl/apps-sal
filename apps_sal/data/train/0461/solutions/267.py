class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = {i: [] for i in range(n)}
        for i in range(len(manager)):
            if manager[i] > -1:
                G[manager[i]].append(i)
        self.ans = 0

        def dfs(root=headID, timeUsed=0):
            if not G[root]:
                return timeUsed
            return max([dfs(child, timeUsed + informTime[root]) for child in G[root]])
        return dfs()
