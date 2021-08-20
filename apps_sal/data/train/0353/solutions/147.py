class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1
        mod = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l) % mod
                l += 1
        return res % mod
