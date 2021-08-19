import math


class Solution:
    def calculateSum(self, nums, divisor):
        Sum = 0
        for num in nums:
            Sum += math.ceil(num / divisor)
        return Sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxValue = max(nums)

        l = 1
        r = maxValue

        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            if mid == maxValue:
                return maxValue

            sum1 = self.calculateSum(nums, mid)
            sum2 = self.calculateSum(nums, mid + 1)
            # print(sum1, sum2)
            if sum2 <= threshold and sum1 > threshold:
                return mid + 1

            if sum1 <= threshold:
                r = mid - 1

            if sum1 > threshold:
                l = mid + 1
        return 1
