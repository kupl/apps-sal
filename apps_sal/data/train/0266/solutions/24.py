class Solution:

    def numSplits(self, s: str) -> int:
        uniqueLeft = 0
        uniqueRight = 0
        ans = 0
        leftDict = {}
        rightDict = {}
        for i in s:
            if i in rightDict:
                rightDict[i] += 1
            else:
                rightDict[i] = 1
                uniqueRight += 1
        for i in s:
            if i in leftDict:
                leftDict[i] += 1
            else:
                leftDict[i] = 1
                uniqueLeft += 1
            rightDict[i] -= 1
            if rightDict[i] == 0:
                uniqueRight -= 1
            if uniqueRight == uniqueLeft:
                ans += 1
        return ans
