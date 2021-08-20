class Solution:

    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        while nums[-1]:
            for (i, num) in enumerate(nums):
                counter += num % 2
                nums[i] = num // 2 * 2
            if nums[-1]:
                nums = [num // 2 for num in nums]
                counter += 1
        return counter
