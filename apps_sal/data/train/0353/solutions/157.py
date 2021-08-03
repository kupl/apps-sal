MOD = 1000000007


class Solution:
    def numSubseq(self, nums, target):
        if not nums:
            return 0
        nums = sorted(nums)
        n = len(nums)
        left, right = 0, n - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                res %= MOD
                left += 1
            else:
                right -= 1
        return res % MOD
