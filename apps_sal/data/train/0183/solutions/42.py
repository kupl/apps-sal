class Solution:
    def maxDotProduct(self, a: List[int], b: List[int]) -> int:
        nums1 = [0] + a
        nums2 = [0] + b
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                # if nums1[j] * nums2[i] > 0:
                dp[i][j] = max(dp[i-1][j-1] + nums1[j] * nums2[i], dp[i][j-1], dp[i-1][j], nums1[j] * nums2[i])
                # else:
                    # dp[i][j] = max(dp[i][j-1], dp[i-1][j], nums1[j] * nums2[i])
        return dp[-1][-1]
