import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = max(nums)
        n = math.floor(math.log(m, 2))
        res = 0
        while n >= 1:
            # print(nums)
            for i, num in enumerate(nums):
                if num >= 2**n:
                    if num % 2 == 1:
                        res += 1
                        nums[i] = (nums[i] - 1) / 2
                    else:
                        nums[i] = nums[i] / 2
            res += 1
            n = n - 1
        for num in nums:
            if num == 1:
                res += 1
        return res
