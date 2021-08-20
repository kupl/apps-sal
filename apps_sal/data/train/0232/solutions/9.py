class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        '\n         res = []\n         for time in timeSeries:\n             if res and res[-1][1] > time:\n                 res[-1][1] = time\n             res.append([time, time+duration])\n         return sum([t[1]-t[0] for t in res])\n         '
        res = 0
        cur = 0
        for time in timeSeries:
            res += min(duration, time + duration - cur)
            cur = time + duration
        return res
