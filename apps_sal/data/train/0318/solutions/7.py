class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        def max_adj_sum(a):
            l = len(a)
            if l == 0:
                return 0
            if l == 1:
                return a[0]
            dp = [[0] * l for i in range(n + 1)]
            for i in range(1, n + 1):
                dp[i][0] = a[0]
                for j in range(1, l):
                    t = dp[i - 1][j - 2] if j >= 2 else 0
                    dp[i][j] = max(dp[i][j - 1], a[j] + t)
            return dp[n][-1]
        return max(max_adj_sum(slices[1:]), max_adj_sum(slices[:-1]))
