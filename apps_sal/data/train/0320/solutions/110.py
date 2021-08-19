class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for (i, num) in enumerate(nums):
                if num % 2:
                    nums[i] -= 1
                    count += 1
            if sum(nums) == 0:
                return count
            for i in range(len(nums)):
                nums[i] //= 2
            count += 1
