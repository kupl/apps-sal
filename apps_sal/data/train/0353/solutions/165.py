class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        res = 0
        mod = (10**9 + 7)
        r = len(sorted_nums) - 1
        for i, left in enumerate(sorted_nums):
            while left + sorted_nums[r] > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r - i))
                res %= mod
        return res
