class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        '''
         res = []
         for time in timeSeries:
             if res and res[-1][1] > time:
                 res[-1][1] = time
             res.append([time, time+duration])
         return sum([t[1]-t[0] for t in res])
         '''
        res = 0
        cur = 0
        for time in timeSeries:
            res += min(duration, time + duration - cur)
            cur = time + duration
        return res
