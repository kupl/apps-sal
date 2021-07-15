class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = []
        maxes = []
        for i in range(len(nums1)):
            dp.append([])
            maxes.append([])
            for j in range(len(nums2)):
                dp[i].append(0)
                maxes[i].append(0)
        for i in range(len(nums1)):
            dp[i][0] = nums1[i] * nums2[0]
            if i > 0:
                dp[i][0] = max(dp[i][0], dp[i-1][0])
        for j in range(len(nums2)):
            dp[0][j] = nums1[0] * nums2[j]
            if j > 0:
                dp[0][j] = max(dp[0][j], dp[0][j-1])
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = max(dp[i-1][j-1] + nums1[i] * nums2[j],
                               nums1[i] * nums2[j])
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                dp[i][j] = max(dp[i][j-1], dp[i][j])
        return dp[-1][-1]
#         dp = []
#         maxes = []
#         for i in range(len(nums1)):
#             dp.append([])
#             maxes.append([])
#             for j in range(len(nums2)):
#                 dp[i].append(0)
#                 maxes[i].append(0)
        
#         for i in range(len(nums1)):
#             dp[i][0] = nums1[i] * nums2[0]
#             maxes[i][0] = nums1[i] * nums2[0]
#             if i > 0:
#                 maxes[i][0] = max(maxes[i-1][0], nums1[i] * nums2[0])
#         for j in range(len(nums2)):
#             dp[0][j] = nums1[0] * nums2[j]
#             maxes[0][j] = nums1[0] * nums2[j]
#             if j > 0:
#                 maxes[0][j] = max(maxes[0][j-1], nums1[0] * nums2[j])
                
#         for i in range(1, len(nums1)):
#             for j in range(1, len(nums2)):
#                 dp[i][j] = max(maxes[i-1][j-1] + nums1[i] * nums2[j],
#                               nums1[i] * nums2[j])
#                 maxes[i][j] = max(maxes[i-1][j-1], maxes[i-1][j])
#                 maxes[i][j] = max(maxes[i][j], maxes[i][j-1])
#                 maxes[i][j] = max(maxes[i][j], dp[i][j])
        
#         return maxes[i][j]

