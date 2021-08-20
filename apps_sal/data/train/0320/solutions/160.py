class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        while nums[-1] != 0:
            if nums[-1] >= 2:
                ans += 1
            for (i, num) in enumerate(nums):
                ans += num % 2
                nums[i] = num // 2
        return ans
