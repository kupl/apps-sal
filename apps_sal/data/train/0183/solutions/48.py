class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        mx, m, n = -math.inf, len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                p = num1 * num2
                mx = max(p, mx)
                p = max(p, 0)
                dp[i + 1][j + 1] = max(dp[i][j] + p, dp[i + 1][j], dp[i][j + 1])

        return mx if mx <= 0 else dp[m][n]
