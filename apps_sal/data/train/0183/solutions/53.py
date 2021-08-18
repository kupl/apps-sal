
import sys


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M = len(nums1)
        N = len(nums2)

        dp = [[-sys.maxsize] * N for _ in range(M)]

        max_p = -sys.maxsize
        for i, num in enumerate(nums2):
            max_p = max(max_p, nums1[0] * nums2[i])
            dp[0][i] = max_p

        max_p = -sys.maxsize
        for i, num in enumerate(nums1):
            max_p = max(max_p, nums1[i] * nums2[0])
            dp[i][0] = max_p

        for i in range(1, M):
            for j in range(1, N):
                x = nums1[i] * nums2[j]
                dp[i][j] = max(x + max(dp[i - 1][j - 1], 0), dp[i - 1][j], dp[i][j - 1])

        return dp[M - 1][N - 1]
