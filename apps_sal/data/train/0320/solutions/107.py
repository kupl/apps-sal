class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        while any(nums):
            for i in range(n):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            if any(nums):
                for i in range(n):
                    nums[i] //= 2
                count += 1
        return count
