class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        last = float('-inf')
        for t in timeSeries:
            total += duration
            if last + duration > t:
                total -= last + duration - t
            last = t
        return total
