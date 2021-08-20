class Solution:

    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        c = 0
        while any(nums):
            for i in range(N):
                if nums[i] & 1:
                    nums[i] -= 1
                    c += 1
            m = max(nums)
            for i in range(N):
                nums[i] >>= 1
            c += 1
        return c - 1
