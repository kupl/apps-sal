class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        for i in range(n1):
            for j in range(n2):
                curr = nums1[i] * nums2[j]
                if i == 0 and j == 0:
                    dp[i][j] = curr
                elif i == 0:
                    dp[i][j] = max(curr, dp[i][j - 1])
                elif j == 0:
                    dp[i][j] = max(curr, dp[i - 1][j])
                else:
                    dp[i][j] = max(curr, curr + dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[n1 - 1][n2 - 1]
