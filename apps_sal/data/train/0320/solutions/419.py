class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        total = 0
        zeros = False
        while sum(nums) > 0:
            for (i, num) in enumerate(nums):
                if num < 1:
                    continue
                zeros = False
                total += num % 2
                nums[i] -= num % 2
            if sum(nums) > 0:
                total += 1
                for (i, num) in enumerate(nums):
                    nums[i] >>= 1
        return total
