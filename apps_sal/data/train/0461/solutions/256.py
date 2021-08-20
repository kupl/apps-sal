class Solution:

    def numOfMinutes(self, n, headID, manager, informTime):
        time_when_informed = {}
        total = 0
        time_when_informed[headID] = 0

        def get_informed_time(node):
            if node in time_when_informed:
                return time_when_informed[node]
            else:
                ret = informTime[manager[node]] + get_informed_time(manager[node])
                time_when_informed[node] = ret
                return ret
        ans = 0
        for node in range(len(manager)):
            if node not in time_when_informed:
                ans = max(ans, get_informed_time(node))
            else:
                ans = max(ans, time_when_informed[node])
        return ans
