class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.max = 0
        directSub = self.makeDirectSub(manager)
        self.dfs(headID, directSub, informTime)
        return self.max

    def makeDirectSub(self, manager):
        d = {new_list: [] for new_list in range(len(manager))}
        for employee in range(len(manager)):
            if manager[employee] != -1:
                d[manager[employee]].append(employee)
        return d

    def dfs(self, headID, directSub, informTime):
        stk = [(headID, 0)]
        while stk:
            (employee, time) = stk.pop()
            self.max = max(self.max, time)
            for subEmp in directSub[employee]:
                stk.append((subEmp, time + informTime[employee]))
        return
