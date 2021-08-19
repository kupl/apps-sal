from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        managerEmployeeTree = defaultdict(list)
        for (i, manager) in enumerate(managers):
            managerEmployeeTree[manager].append(i)
        return self._traversal(managerEmployeeTree, headID, informTime)

    def _traversal(self, managerEmployeeTree, manager, informTime):
        if managerEmployeeTree.get(manager):
            maxInformTime = 0
            for employee in managerEmployeeTree[manager]:
                employeeInformTime = self._traversal(managerEmployeeTree, employee, informTime)
                maxInformTime = max(maxInformTime, employeeInformTime)
            return informTime[manager] + maxInformTime
        return 0
