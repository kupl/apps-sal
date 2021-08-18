from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.max = 0
        directSub = self.makeDirectSub(n, manager)
        self.dfs(headID, directSub, informTime)
        return self.max

    def makeDirectSub(self, n, manager):
        d = defaultdict(list)
        for sub, employee in enumerate(manager):
            d[employee].append(sub)
        return d

    def dfs(self, headID, directSub, informTime):
        stk = [(headID, 0)]
        while stk:
            employee, time = stk.pop()
            self.max = max(self.max, time)
            for subEmp in directSub[employee]:
                stk.append((subEmp, time + informTime[employee]))
        return
