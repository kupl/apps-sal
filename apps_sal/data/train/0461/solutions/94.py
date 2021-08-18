class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = {}
        if len(manager) == 1:
            return informTime[-1]
        for i in range(n):
            adj[i] = []

        for idx, i in enumerate(manager):
            if i == -1:
                continue
            adj[i].append([idx, informTime[idx]])
        ans = [-10**10]

        def dfs(curr, cost):
            ans[-1] = max(ans[-1], cost)
            for i in range(len(adj[curr])):
                dfs(adj[curr][i][0], cost + adj[curr][i][1])

        dfs(headID, informTime[headID])
        return ans[-1]
