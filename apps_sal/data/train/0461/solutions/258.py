class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # DFS, find longest path from root to leaf
        #TC: O(N)
        #SC: O(N)
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
            # time taken for the information to reach i
            # print(i, child[i])
            res = max(res, time)
            for j in range(len(child[i])):
                dfs(child[i][j], time + informTime[i])
        dfs(boss, 0)
        return res
