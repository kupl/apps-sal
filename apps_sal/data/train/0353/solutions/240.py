class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        l, r = 0, n - 1
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1
        return ans % mod
