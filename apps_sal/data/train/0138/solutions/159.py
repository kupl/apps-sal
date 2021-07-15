class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        product = 1
        count = 0
        firstNegative = -1
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                if firstNegative == -1:
                    firstNegative = i
            
            if nums[i] == 0:
                count = 0
                product = 1
                firstNegative = -1

            else:
                product*=nums[i]
                count+=1
                if product > 0:
                    maxCount = max(maxCount, count)
                else:
                    if firstNegative!=-1:
                        maxCount = max(maxCount, i-firstNegative)
        return maxCount

