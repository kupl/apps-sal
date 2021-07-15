  
class Solution:
    # 1152
    def numOfMinutes(self, n, headID, manager, informTime):
       # @lru_cache(None)
        def myTime(myBoss):
            if manager[myBoss] > -1:
                informTime[myBoss] += myTime(manager[myBoss])
                manager[myBoss] = -1
                
            return informTime[myBoss]
        return max(map(myTime, manager))
