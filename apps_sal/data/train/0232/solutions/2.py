class Solution:

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        if timeSeries == []:
            return 0
        last = timeSeries[0]
        cur = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - cur < duration:
                cur = timeSeries[i]
                continue
            else:
                res += cur - last + duration
                last = timeSeries[i]
                cur = timeSeries[i]
        res += cur - last + duration
        return res
