class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans, mod = 0, 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1
        return ans % mod
