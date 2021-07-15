class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*len(nums2) for _ in nums1]
        res=-float('inf')
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i==0 or j==0:
                    if i==0 and j==0:
                        dp[i][j]=nums1[i]*nums2[j]
                    elif i==0:
                        dp[i][j]=max(dp[i][j-1],nums1[i]*nums2[j])
                    else:
                        dp[i][j]=max(dp[i-1][j],nums1[i]*nums2[j])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],nums1[i]*nums2[j],nums1[i]*nums2[j]+dp[i-1][j-1])
            res=max(res,dp[i][-1])
        #print(dp)
        return res
