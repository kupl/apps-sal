class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def helper(i, manager, informTime):
            if manager[i] != -1:
                informTime[i] += helper(manager[i], manager, informTime)
                manager[i] = -1
            return informTime[i]

        res = 0
        for i in range(n):
            res = max(res, helper(i, manager, informTime))
        return res
