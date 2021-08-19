class Solution:

    def numSplits(self, s: str) -> int:
        leftMap = {}
        rightMap = {}
        for j in range(len(s)):
            rightMap[s[j]] = rightMap.get(s[j], 0) + 1
        i = 0
        result = 0
        while i < len(s) - 1:
            leftMap[s[i]] = leftMap.get(s[i], 0) + 1
            rightMap[s[i]] = rightMap[s[i]] - 1
            if rightMap.get(s[i], 0) <= 0:
                rightMap.pop(s[i])
            if len(leftMap) == len(rightMap):
                result += 1
            i += 1
        return result
