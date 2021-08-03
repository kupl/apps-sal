class Solution:
    # 1152 ms
    def numOfMinutes(self, n, headID, manager, informTime):
        @lru_cache(None)
        def myTime(myBoss):
            if manager[myBoss] > -1:
                informTime[myBoss] += myTime(manager[myBoss])
              #  t2 =
                manager[myBoss] = -1
               # return t1 + t2
            return informTime[myBoss]
        return max(map(myTime, manager))
