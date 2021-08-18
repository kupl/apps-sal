class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        dp[0][0] = max(0, nums1[0] * nums2[0])

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + nums1[i] * nums2[j])
                else:
                    if j > 0 and i == 0:
                        dp[i][j] = max(dp[i][j - 1], nums1[i] * nums2[j])
                    if i > 0 and j == 0:
                        dp[i][j] = max(dp[i - 1][j], nums1[i] * nums2[j])

        ans = max([max(x) for x in dp])

        if ans > 0:
            return ans
        else:
            best = -9999999
            for k in nums1:
                for l in nums2:
                    best = max(best, k * l)

            return best
