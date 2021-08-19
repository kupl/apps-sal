class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        l = 0
        h = len(nums) - 1
        MOD = 10 ** 9 + 7
        while l <= h:
            if nums[l] + nums[h] <= target:
                ans = (ans + pow(2, h - l, MOD)) % MOD
                l += 1
            else:
                h -= 1
        return ans
