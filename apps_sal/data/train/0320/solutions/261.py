class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ops = 0

        if not any(n != 0 for n in nums):
            return 0

        while nums:
            if any((n % 2 != 0) for n in nums):
                for idx, n in enumerate(nums):
                    if nums[idx] % 2 != 0:
                        nums[idx] -= 1
                        ops += 1
                nums = [n for n in nums if n != 0]
            else:
                ops += 1
                nums = [int(n / 2) for n in nums]

        return ops
