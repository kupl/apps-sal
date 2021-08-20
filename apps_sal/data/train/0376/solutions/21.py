class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:

        def dfs(nums, i, j):
            if j - i <= 1:
                return 0
            key = tuple([i, j])
            if key in dp:
                return dp[key]
            ans = sys.maxsize
            for k in range(i + 1, j):
                ans = min(ans, dfs(nums, i, k) + dfs(nums, k, j) + nums[i] * nums[k] * nums[j])
            dp[key] = ans
            return ans
        dp = {}
        total = dfs(A, 0, len(A) - 1)
        return total
