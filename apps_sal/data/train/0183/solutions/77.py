class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[-math.inf] * (n) for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                dp[i][j] = max(dp[i][j], nums1[i] * nums2[j])
                if i > 0 and j > 0 and dp[i - 1][j - 1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i] * nums2[j])

        return dp[m - 1][n - 1]
