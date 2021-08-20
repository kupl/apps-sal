class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        mod = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l)
                l += 1
        return res % mod
