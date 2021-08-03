class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        while any(n > 0 for n in nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
            if all(n == 0 for n in nums):
                break
            nums = [n // 2 for n in nums]
            count += 1

        return count
