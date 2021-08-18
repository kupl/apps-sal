class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = collections.defaultdict(set)
        for e, m in enumerate(manager):
            g[m].add(e)

        visited = dict()

        def dfs(node):

            total = 0
            for nei in g[node]:
                total = max(total, dfs(nei) + informTime[node])
            return total

        return dfs(headID)
