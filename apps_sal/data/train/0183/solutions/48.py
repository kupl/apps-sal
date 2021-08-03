class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #         Target: We want to calculate the maximal dot product for nums1[0:i] and nums2[0:j]
        # Base case
        # When i == 0 or j == 0, we return -inf. (Because this is an empty case, which is intolerable)
        # State Transition, for any i > 0 and j > 0, there are 4 possibilities
        # nums1[i - 1] is not selected, dp[i][j] = dp[i - 1][j]
        # nums2[j - 1] is not selected, dp[i][j] = dp[i][j - 1]
        # Neither nums1[i - 1] or nums2[j - 1] is selected, dp[i][j] = dp[i - 1][j - 1]
        # Both nums1[i - 1] and nums2[j - 1] are selected, dp[i][j] = max(dp[i - 1][j - 1], 0) + nums1[i - 1] * nums2[j - 1]
        # Since we already selected one pair (nums1[i - 1], nums2[j - 1]), we can assume the minimal proceeding value is 0
        mx, m, n = -math.inf, len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                p = num1 * num2
                mx = max(p, mx)
                p = max(p, 0)
                dp[i + 1][j + 1] = max(dp[i][j] + p, dp[i + 1][j], dp[i][j + 1])

        return mx if mx <= 0 else dp[m][n]

        # n, m = len(nums1), len(nums2)
        # dp = [-math.inf] * (m + 1)
        # for i in range(1, n + 1):
        #     dp, old_dp = [-math.inf], dp
        #     for j in range(1, m + 1):
        #         dp += max(
        #             old_dp[j], # not select i
        #             dp[-1], # not select j
        #             old_dp[j - 1], # not select either
        #             max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # select both
        #         ),
        # return dp[-1]
