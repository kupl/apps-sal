class Employee:
    def __init__(self, employeeID, informTime):
        self.id = employeeID
        self.informTime = informTime 
        self.sub = []
    
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]
        
        head = self.buildEmpTree(n, manager, headID, informTime)
        
        return self.maxTime(head)
        
    def buildEmpTree(self, n, manager, headID, informTime):
        s = {}
        for i in range(n):
            s[i] = Employee(i, informTime[i])
            
        for i in range(n):
            if manager[i] == -1:
                continue
            s[manager[i]].sub.append(s[i])
                    
        return s[headID]
        
    def maxTime(self, root):
        if not root.sub:
            return root.informTime
        
        curMax = root.informTime
        
        for subordinate in root.sub:
            curMax = max(curMax, root.informTime + self.maxTime(subordinate))
        
        return curMax

