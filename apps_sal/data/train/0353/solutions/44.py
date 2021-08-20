class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        r = len(nums) - 1
        for l in range(len(nums)):
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                ans += 1 << r - l
                ans %= MOD
        return ans
