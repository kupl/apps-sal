class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        negIndex = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pos = 0
                neg = 0
            elif nums[i] > 0:
                pos += 1
            else:
                neg += 1
                if neg == 1:
                    negIndex = i
                
            if neg % 2 == 0:
                res = max(res, pos + neg)
            else:
                res = max(res, i - negIndex)
        return res 

