MOD = 10**9 + 7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res = (res + pow(2, r - l)) % MOD
                l += 1

        return res
