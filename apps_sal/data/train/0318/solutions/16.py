class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:

        def helper(start, end):
            dp = [[0] * n for _ in range(end - start + 1)]
            dp[0] = [slices[start]] * n
            dp[1] = [max(slices[start], slices[start + 1])] * n
            for i in range(start + 2, end + 1):
                dp[i - start][0] = max(slices[i], dp[i - start - 1][0])
                for j in range(1, n):
                    dp[i - start][j] = max(dp[i - start - 1][j], slices[i] + dp[i - start - 2][j - 1])
            return dp[-1][-1]
        n = len(slices) // 3
        return max(helper(0, len(slices) - 2), helper(1, len(slices) - 1))
