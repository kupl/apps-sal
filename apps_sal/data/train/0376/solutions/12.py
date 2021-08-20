class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:

        def dfs(nums, i, j):
            if j - i <= 1:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            ans = sys.maxsize
            for k in range(i + 1, j):
                ans = min(ans, dfs(nums, i, k) + dfs(nums, k, j) + nums[i] * nums[k] * nums[j])
            dp[i][j] = ans
            return ans
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        total = dfs(A, 0, len(A) - 1)
        return total
