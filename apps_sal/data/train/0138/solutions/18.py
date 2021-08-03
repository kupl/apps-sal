class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        negNum = 0
        firstNegIdx = -1
        zeroPos = -1
        res = 0

        for i, num in enumerate(nums):
            if num < 0:
                negNum += 1
                if firstNegIdx < 0:
                    firstNegIdx = i

            if num == 0:
                negNum = 0
                firstNegIdx = -1
                zeroPos = i
            else:
                if negNum % 2 == 0:
                    res = max(res, i - zeroPos)
                else:
                    res = max(res, i - firstNegIdx)

        return res
