class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        idx = {n: i for i, n in enumerate(nums)}
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = 2
            dp[j][j] = 1
        for i in range(1, n):
            for j in range(i + 1, n):
                dp[i][j] = 2
                if nums[i] > nums[j] // 2 and nums[j] - nums[i] in idx:
                    ii = idx[nums[j] - nums[i]]
                    dp[i][j] = dp[ii][i] + 1
                ans = max(ans, dp[i][j])
        return ans if ans > 2 else 0
