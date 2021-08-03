class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[[0, 0] for i in range(n2)] for j in range(n1)]

        for i in range(n1):
            for j in range(n2):
                if i == 0:
                    if j == 0:
                        dp[i][j] = nums1[i] * nums2[j]

                    else:
                        dp[i][j] = max(dp[i][j - 1], nums1[i] * nums2[j])

                elif j == 0:
                    dp[i][j] = max(dp[i - 1][j], nums1[i] * nums2[j])

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], nums1[i] * nums2[j] + dp[i - 1][j - 1], dp[i - 1][j - 1], nums1[i] * nums2[j])

        return dp[-1][-1]
