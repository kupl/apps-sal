class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        length = len(timeSeries)
        if length == 1:
            return duration
        result = duration
        (start_time, end_time) = (timeSeries[0], timeSeries[0] + duration - 1)
        for t in timeSeries[1:]:
            if t <= end_time:
                result += t + duration - 1 - end_time
                end_time = t + duration - 1
            else:
                result += duration
                (start_time, end_time) = (t, t + duration - 1)
        return result
