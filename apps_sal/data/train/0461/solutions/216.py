class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        times = n * [-1]

        def dfs(v):
            times[v] = informTime[v]
            if manager[v] == -1:
                return times[v]
            parent = manager[v]
            if times[parent] != -1:
                times[v] += times[parent]
                return times[v]
            else:
                times[v] += dfs(parent)
                return times[v]
        for (i, _emp) in enumerate(manager):
            if times[i] == -1:
                dfs(i)
        return max(times)
