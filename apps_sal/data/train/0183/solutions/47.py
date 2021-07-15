class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i][j] = nums1[i] * nums2[j]
                
                if i and j:
                    dp[i][j] += max(0, dp[i-1][j-1])
                    
                if i:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                    
                if j:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[-1][-1]
