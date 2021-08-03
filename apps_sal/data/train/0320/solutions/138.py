class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        while sum(nums):
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] = nums[i] - 1
                    ans += 1
            if sum(nums):
                nums = [o / 2 for o in nums]
                ans += 1
        return ans
