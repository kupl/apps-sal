class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (l, r) = (0, len(nums) - 1)
        (res, mod) = (0, 10 ** 9 + 7)
        while l <= r:
            sum_ = nums[l] + nums[r]
            if sum_ <= target:
                res += 2 ** (r - l) % mod
                l += 1
            else:
                r -= 1
        return res % mod
