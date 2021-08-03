class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        employeesDict = {}

        for i in range(0, len(manager)):

            if manager[i] == -1:
                continue

            if manager[i] in employeesDict:
                employeesDict[manager[i]].append(i)
            else:
                l = []
                l.append(i)
                employeesDict[manager[i]] = l

        return self.helper(headID, informTime[headID], employeesDict, informTime)

    def helper(self, currEmp, currTime, employeesDict, informTime):

        if currEmp not in employeesDict:
            return currTime
        newTime = -1
        managerList = employeesDict[currEmp]
        for i in range(0, len(managerList)):

            newTime = max(newTime, self.helper(managerList[i], informTime[managerList[i]], employeesDict, informTime) + currTime)

        return newTime
