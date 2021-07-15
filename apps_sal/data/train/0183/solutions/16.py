class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        M = len(nums1)
        N = len(nums2)
        
        dp = [[0] * N for _ in range(M)]
        
        dp[0][0] = nums1[0] * nums2[0]
        
        for i in range(1, M):
            dp[i][0] = max(dp[i-1][0], nums2[0] * nums1[i])
            
        for i in range(1, N):
            dp[0][i] = max(dp[0][i-1], nums1[0] * nums2[i])
            
        
        for i in range(1, M):
            for j in range(1, N):
                
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-1] + nums1[i]*nums2[j], dp[i-1][j], dp[i][j-1], nums1[i]*nums2[j])
        
            
        return dp[-1][-1]
