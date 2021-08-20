class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        return sum((min(duration, b - a) for (a, b) in zip(timeSeries, timeSeries[1:] + [100000000.0])))
