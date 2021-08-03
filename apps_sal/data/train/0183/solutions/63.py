class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        # (i,j)到当前位置的最大子序列乘积和
        for i in range(m):
            for j in range(n):
                dp[i][j] = nums1[i] * nums2[j]
                if i > 0 and j > 0:  # 此时判断是否与前边连接
                    dp[i][j] += max(0, dp[i - 1][j - 1])
                # 当前i,j只取一个
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]

# 类似于72：编辑距离
# dp[i][j]代表nums1到i位，nums2到j位的最大乘积和
# 由于是子序列，要判断取i还是取j,以及前边的子序列要不要取
