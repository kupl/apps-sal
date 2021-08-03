class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        l = len(timeSeries)
        if l == 0:
            return 0
        if l == 1:
            return duration

        T = 0
        i = 1
        while i < l:
            if timeSeries[i] - timeSeries[i - 1] >= duration:
                T += duration
            else:
                T += timeSeries[i] - timeSeries[i - 1]
            i += 1
        T += duration
        return T
