class Solution: 

    def processEmployee(self, employee, managerOfEmployee, informTime, dp):
        if employee == -1 or dp[employee]: return employee
        dp[employee] = 1
        managerOfEmployee[employee] = self.processEmployee(managerOfEmployee[employee], managerOfEmployee, informTime, dp)
        if managerOfEmployee[employee] != -1: informTime[employee] += informTime[managerOfEmployee[employee]]
        return employee
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dp = [0] * (n + 1)
        for employee in range(n): self.processEmployee(employee, manager, informTime, dp)                          
        return max(informTime)
