class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while max(nums) != 0:
            allEven = True
            for i, n in enumerate(nums):
                if n % 2 == 1:
                    nums[i] -= 1
                    op += 1
                    allEven = False
            if allEven:
                nums = [n // 2 for n in nums]
                op += 1
        return op
