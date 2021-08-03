class Solution:
    res = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if not manager or not informTime:
            return 0
        dic = {-1: [[headID, informTime[headID]]]}
        for i in range(len(manager)):
            if manager[i] not in dic:
                dic[manager[i]] = []
            dic[manager[i]].append([i, informTime[i]])

        def dfs(dic: {}, id: int, cur: int) -> None:
            if id not in dic:
                self.res = max(self.res, cur)
                return

            for employee in dic[id]:
                dfs(dic, employee[0], cur + employee[1])

        dfs(dic, -1, 0)

        return self.res
