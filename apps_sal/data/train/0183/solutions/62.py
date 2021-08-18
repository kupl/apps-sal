class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * (n2) for j in range(n1)]
        for i in range(n1):
            for j in range(n2):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]
