class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def canMakeBouquet(m, k, bloomDay, currDay):
            numBouquets = 0
            slidingWindowLen = 0
            for i in range(0, len(bloomDay)):
                if bloomDay[i] <= currDay:
                    slidingWindowLen += 1
                else:
                    slidingWindowLen = 0
                if slidingWindowLen == k:
                    numBouquets += 1
                    slidingWindowLen = 0
            return numBouquets >= m
        lowBound = 1
        highBound = max(bloomDay)
        while lowBound < highBound:
            midBound = lowBound + (highBound - lowBound) // 2
            if not canMakeBouquet(m, k, bloomDay, midBound):
                lowBound = midBound + 1
            else:
                highBound = midBound
        if canMakeBouquet(m, k, bloomDay, lowBound):
            return lowBound
        else:
            return -1
