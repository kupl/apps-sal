class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1
        return ans % mod
