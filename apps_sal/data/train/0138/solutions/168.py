class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        product = 1
        count = 0
        firstNegative = -1
        maxCount = -math.inf
        for i in range(len(nums)):
            if nums[i] > 0:
                product *= nums[i]
                count += 1
            elif nums[i] < 0:
                product *= nums[i]
                count += 1
                if firstNegative == -1:
                    firstNegative = i

            if nums[i] == 0:
                count = 0
                product = 1
                if firstNegative != -1 and i - firstNegative - 1 > maxCount:
                    maxCount = i - firstNegative - 1
                firstNegative = -1

            if product > 0:
                maxCount = max(maxCount, count)

        if firstNegative != -1 and i - firstNegative > maxCount:
            maxCount = i - firstNegative
        return maxCount
