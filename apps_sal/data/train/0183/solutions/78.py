def maxsub(a,b):
    dp = [[0 for x in range(len(b))] for x in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b)):
            dp[i][j] = a[i]*b[j]
            if i-1>=0:
                dp[i][j] = max(dp[i][j],dp[i-1][j] )
            if j-1>=0:
                dp[i][j] = max(dp[i][j],dp[i][j-1] )
            if i-1>=0 and j-1>=0:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+a[i]*b[j] )
    return dp[-1][-1]
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return maxsub(nums1, nums2)
