class Solution:

    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        while not all(n == 0 for n in nums):
            if all(n % 2 == 0 for n in nums):
                nums = [n / 2 for n in nums]
                operations += 1
            else:
                for i, num in enumerate(nums):
                    if num % 2 != 0:
                        nums[i] = num - 1
                        operations += 1
        return operations
