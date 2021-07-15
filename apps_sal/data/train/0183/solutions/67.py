MAX_VAL = -10 ** 9 - 7
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        num_rows = len(nums1) + 1
        num_cols = len(nums2) + 1
        
        dp = []
        for i in range(num_rows):
            dp.append([MAX_VAL] * num_cols)
            
        
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + nums1[i-1] * nums2[j-1], nums1[i-1] * nums2[j-1])
        return dp[-1][-1]
