class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        prev = timeSeries[0]
        ret = 0
        count = 0
        for t in timeSeries[1:]:
            diff = t - prev
            if diff > duration:
                count += 1
            else:
                ret += diff
            prev = t
        ret += (count + 1) * duration
        return ret
