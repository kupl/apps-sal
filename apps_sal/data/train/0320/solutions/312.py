class Solution:

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        while True:
            for (i, x) in enumerate(nums):
                if x & 1:
                    result += 1
                    nums[i] -= 1
            if all((x == 0 for x in nums)):
                return result
            for (i, x) in enumerate(nums):
                nums[i] //= 2
            result += 1
