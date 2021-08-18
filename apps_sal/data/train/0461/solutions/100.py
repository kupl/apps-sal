class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        @lru_cache(None)
        def myTime(myBoss):
            if manager[myBoss] > -1:
                t1 = informTime[myBoss]
                t2 = myTime(manager[myBoss])
                return t1 + t2
            return informTime[headID]
        return max(map(myTime, manager))
