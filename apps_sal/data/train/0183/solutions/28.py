class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        dp = [[0] * M for _ in range(N)]
        
        dp[0][0] = nums1[0] * nums2[0]
        res = dp[0][0]
        
        big = nums1[0] >= 0
        acc = nums2[0]
        for i, x in enumerate(nums2[1:]):
            if big and x > acc:
                acc = x
            elif not big and x < acc:
                acc = x
            
            dp[0][i+1] = acc * nums1[0]
            res = max(res, dp[0][i+1])
        
        big = nums2[0] >= 0
        acc = nums1[0]
        for i, x in enumerate(nums1[1:]):
            if big and x > acc:
                acc = x
            elif not big and x < acc:
                acc = x
            
            dp[i+1][0] = acc * nums2[0]
            res = max(res, dp[i+1][0])
        
        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], nums1[i] * nums2[j] + max(0, dp[i-1][j-1]))
                
                res = max(res, dp[i][j]) 
        
        return res
