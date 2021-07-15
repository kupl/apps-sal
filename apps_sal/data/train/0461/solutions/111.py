class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]
        
        s = collections.defaultdict(list)
        for i in range(n):
            if manager[i] == -1:
                continue
            s[manager[i]].append(i)
        
        return self.maxTime(s, informTime, headID)
    
        
    def maxTime(self, employeeMap, informTime, curID):
        if not employeeMap[curID]:
            return informTime[curID]
        
        curMax = informTime[curID]
        
        for subordinate in employeeMap[curID]:
            curMax = max(curMax, informTime[curID] + self.maxTime(employeeMap, informTime, subordinate))
        
        return curMax

