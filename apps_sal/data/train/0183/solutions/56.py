class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = nums1[0]*nums2[0]
        for i in range(1,m):
            dp[0][i] = max(dp[0][i-1],nums1[0]*nums2[i])
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],nums2[0]*nums1[i])
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+nums1[i]*nums2[j],nums1[i]*nums2[j])
        return dp[-1][-1]
