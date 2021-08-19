class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        m = sum(nums)
        N = len(nums)

        @lru_cache(None)
        def dp(i, p):  # best sumsofar at i
            if i == N:
                return 0 if p == 0 else -float('inf')

            a = dp(i + 1, p)
            b = dp(i + 1, (p + nums[i]) % 3) + nums[i]
            return max(a, b)

        return dp(0, 0)
