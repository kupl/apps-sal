class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) >= len(nums) - 1:
            return len(nums) - 1

        l = 0
        while nums[l] == 0:
            l += 1
            if l == len(nums):
                return 0

        r = l + 1
        sum_total = nums[l]
        res = 0
        for r in range(r, len(nums)):
            sum_total += nums[r]
            if sum_total == r - l - 1:
                res = max(res, sum_total)
                while sum_total < r - l:
                    sum_total -= nums[l]
                    l += 1

        return max(res, sum_total)
