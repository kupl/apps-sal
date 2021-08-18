class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0
        nums.sort()
        res = 0
        mod = 10**9 + 7

        l, r = 0, len(nums) - 1
        while l <= r:

            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res = (res + pow(2, r - l, mod)) % mod
                l += 1
        return res
