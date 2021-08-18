class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        l, r, res = 0, n - 1, 0
        dp = [1] * n
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1]) % (1000000007)
        while l <= r:
            while nums[l] + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                res += 1
                res += dp[r - l] - 1
                l += 1

        return res % (1000000007)
