class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(g, u, informTime, time):
            total_time = time
            for v in g[u]:
                if v != -1:
                    total_time = max(total_time, dfs(g, v, informTime, time + informTime[v]))

            return total_time

        g = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                g[m].append(i)

        return dfs(g, headID, informTime, informTime[headID])
