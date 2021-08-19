class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total_poisoned_time = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] <= timeSeries[i] + duration:
                total_poisoned_time += timeSeries[i + 1] - timeSeries[i]
            else:
                total_poisoned_time += duration
        total_poisoned_time += duration
        return total_poisoned_time
