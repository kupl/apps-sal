class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = 0
        nums.sort()
        M = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + pow(2, r - l, M)) % M
                l += 1
            else:
                r -= 1
        return res
