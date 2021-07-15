class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managerMapping = {}
        maxTime = 0
        def dfs(currentTime, currentEmployee, manangerMapping):
            nonlocal maxTime
            if currentEmployee not in managerMapping:
                maxTime = max(currentTime, maxTime)
            else:
                directs = managerMapping[currentEmployee]
                for direct in directs:
                    dfs(currentTime + informTime[currentEmployee], direct, managerMapping)
                    
        for i in range(len(manager)):
            if manager[i] in managerMapping:
                managerMapping[manager[i]].append(i)
            else:
                managerMapping[manager[i]] = [i]
        dfs(0, headID, managerMapping)
        return maxTime
