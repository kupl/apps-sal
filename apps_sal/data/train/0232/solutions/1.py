class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        previous_time = timeSeries[0]
        total_time = duration
        for time in timeSeries[1:]:
            if time - previous_time < duration:
                total_time += time - previous_time
                previous_time = time
            else:
                total_time += duration
                previous_time = time
        return total_time
