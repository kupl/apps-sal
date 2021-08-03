class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = nums1[i] * nums2[j]
                elif i == 0:
                    dp[i][j] = max(dp[i][j - 1], nums1[i] * nums2[j])
                elif j == 0:
                    dp[i][j] = max(dp[i - 1][j], nums1[i] * nums2[j])
                else:
                    temp = nums1[i] * nums2[j]
                    dp[i][j] = max(temp, dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + temp)
        return dp[-1][-1]
