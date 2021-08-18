class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hoursLen = len(hours)
        tDay = []
        preSum = 0
        preSumDict = {0: -1}
        preSumKeys = [0]
        ans = 0

        def insertAt(x):
            l = 0
            r = len(preSumKeys) - 1
            if x < preSumKeys[l]:
                return 0
            if x > preSumKeys[r]:
                return r + 1
            while r > l:
                m = (r + l) // 2
                if preSumKeys[m] < x:
                    l = m + 1
                else:
                    r = m
            return l

        ans = 0
        for i, hour in enumerate(hours):
            if hour > 8:
                tDay.append(1)
                preSum += 1
            else:
                tDay.append(-1)
                preSum -= 1
            tempIndex = insertAt(preSum)
            if preSum not in preSumDict:
                preSumDict[preSum] = i
                preSumKeys.insert(tempIndex, preSum)
            if tempIndex > 0:
                preSumDict[preSumKeys[tempIndex]] = min(preSumDict[preSumKeys[tempIndex - 1]], preSumDict[preSumKeys[tempIndex]])
                ans = max(ans, i - preSumDict[preSumKeys[tempIndex - 1]])
        return ans
