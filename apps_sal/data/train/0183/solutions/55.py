class Solution:
    def maxDotProduct(self, nums1, nums2):
        if all(x >= 0 for x in nums1) and all(y <= 0 for y in nums2):
            return min(nums1) * max(nums2)
        if all(x <= 0 for x in nums1) and all(y >= 0 for y in nums2):
            return max(nums1) * min(nums2)
        a, b = len(nums1), len(nums2)
        dp = [[0 for _ in range(b)] for _ in range(a)]
        for i in range(a):
            for j in range(b):
                dp[i][j] = nums1[i] * nums2[j]
                if i: dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j-1])
                if i and j: dp[i][j] = max(dp[i][j], nums1[i] * nums2[j] + dp[i-1][j-1])
        return dp[a-1][b-1]
