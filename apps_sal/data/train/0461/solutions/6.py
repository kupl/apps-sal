class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1 and manager[0] == -1:
            return informTime[0]
        subordinates = defaultdict(list)
        for empId in range(len(manager)):
             subordinates[manager[empId]].append(empId)
        def dfs(sid,informTime):
            maxtime = 0
            for subId in subordinates[sid]:
                maxtime = max(maxtime,dfs(subId,informTime))
            return (maxtime+informTime[sid])
        return dfs(headID,informTime)
            

