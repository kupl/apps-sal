class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(node, cost):
            nonlocal ans
            cost += informTime[node]
            ans = max(ans, cost)
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei, cost)
        graph = collections.defaultdict(list)
        for (i, man) in enumerate(manager):
            if man == -1:
                continue
            graph[man].append(i)
        seen = set()
        ans = 0
        dfs(headID, 0)
        return ans
