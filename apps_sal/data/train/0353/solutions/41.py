class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        (l, r) = (0, len(nums) - 1)
        MOD = 10 ** 9 + 7
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res = (res + (1 << r - l)) % MOD
                l += 1
        return res
