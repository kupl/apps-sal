class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-sys.maxsize-1 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                t = nums1[i-1]*nums2[j-1]
                dp[i][j] = max({dp[i-1][j-1]+t,t,dp[i-1][j], dp[i][j-1]})
        # print(dp)
        return dp[-1][-1]

