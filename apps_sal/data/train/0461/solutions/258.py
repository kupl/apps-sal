class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = defaultdict(list)
        boss = -1
        res = 0
        for i in range(len(manager)):
            if manager[i] == -1:
                boss = i
                continue
            child[manager[i]].append(i)

        def dfs(i, time):
            nonlocal res
            res = max(res, time)
            for j in range(len(child[i])):
                dfs(child[i][j], time + informTime[i])
        dfs(boss, 0)
        return res
