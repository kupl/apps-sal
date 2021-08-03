class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        if not nums or target == 0:
            return 0

        nums.sort()

        l, r = 0, len(nums) - 1
        mod = 10**9 + 7
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += (2**(r - l)) % mod
                l += 1
        return res % mod
