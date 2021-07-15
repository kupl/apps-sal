from collections import deque
class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        memo = [None] * n
        memo[headID] = 0
        for uid in range(n):
            self.dfs(uid, manager, informTime, memo)
        return max(memo)
    
    def dfs(self, uid, manager, informTime, memo):
        if memo[uid] is not None:
            return memo[uid]
        
        memo[uid] = self.dfs(manager[uid], manager, informTime, memo) + informTime[manager[uid]]
        return memo[uid]
