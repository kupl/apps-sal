class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)) for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(i == 0 and j == 0):
                    dp[i][j] = nums1[0]*nums2[0]
                    continue
                prod = nums1[i]*nums2[j]
                if(i == 0):
                    dp[i][j] = max(dp[i][j-1], prod)
                    continue
                if(j == 0):
                    dp[i][j] = max(dp[i-1][j], prod)
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+prod, prod)
        return dp[-1][-1]
