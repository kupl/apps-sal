class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        (a, b) = ([None] + nums1, [None] + nums2)
        (m, n) = (len(a), len(b))
        dp = [[-math.inf] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                here = a[i] * b[j]
                dp[i][j] = max(here, dp[i - 1][j - 1] + max(here, 0), dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
