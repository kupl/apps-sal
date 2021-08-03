class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        totalBlind = 0
        lastBlindEnd = 0
        ts = sorted(timeSeries)
        for time in ts:
            if time < lastBlindEnd:
                totalBlind += time + duration - lastBlindEnd
            else:
                totalBlind += duration
            lastBlindEnd = time + duration
        return totalBlind
