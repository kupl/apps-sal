class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        n, m = len(nums1), len(nums2)

        dp1 = [[-float('inf')] * (m) for _ in range(n)]
        dp2 = [[-float('inf')] * (m) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dp1[i][j] = nums1[i] * nums2[j]
                if i != 0 and j != 0:
                    dp1[i][j] = max(dp1[i][j], dp2[i-1][j-1] + nums1[i] * nums2[j])

                dp2[i][j] = dp1[i][j]
                if i != 0:
                    dp2[i][j] = max(dp2[i][j], dp2[i-1][j])
                if j != 0:
                    dp2[i][j] = max(dp2[i][j], dp2[i][j-1])

        ans = -float('inf')
        for i in range(n):
            for j in range(m):
                ans = max(ans, dp2[i][j])
        return ans

