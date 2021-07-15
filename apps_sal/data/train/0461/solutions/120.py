class Solution:
    def __init__(self):
        self.result = -1
        self.reports_map = defaultdict(list)
        
    def notifyReport(self, managerID: int, timeSpent: int, informTime: List[int]):
        if managerID not in self.reports_map:
            if self.result == -1 or timeSpent > self.result:
                self.result = timeSpent
        else:
            for report in self.reports_map[managerID]:
                self.notifyReport(report, timeSpent + informTime[managerID], informTime)
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        for i in range(0, len(manager)):
            self.reports_map[manager[i]].append(i)
        
        self.notifyReport(headID, 0, informTime)
        
        return self.result
