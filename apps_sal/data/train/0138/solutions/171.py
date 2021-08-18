class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        accLast = 1
        accCurr = 1
        lastpos = 0
        lastnegative = -1
        res = 0
        dic = {}
        for i in range(len(nums)):
            accCurr = accLast * nums[i]
            if accCurr == 0:
                lastpos = i + 1
                lastnegative = -1
                accCurr = 1
            elif accCurr > 0:
                if lastpos != -1:
                    res = max(res, i + 1 - lastpos)
            else:
                if lastnegative != -1:
                    res = max(res, i + 1 - lastnegative)
                else:
                    lastnegative = i + 1
            accLast = accCurr
        return res
