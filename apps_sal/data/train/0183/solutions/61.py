
import sys
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        result = -sys.maxsize
        len1 = len(nums1)
        len2 = len(nums2)
        dp = [[-sys.maxsize for j in range(len2)] for i in range(len1)]
        for i in range(0, len1):
            for j in range(0, len2):
                dp[i][j] = nums1[i] * nums2[j]
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i] * nums2[j])
                result = max(result, dp[i][j])
                pass
            pass
        return result
