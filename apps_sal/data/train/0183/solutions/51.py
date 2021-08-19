class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = collections.defaultdict(lambda: -math.inf)
        for (i, j) in product(range(len(nums1)), range(len(nums2))):
            (x, y) = (nums1[i] * nums2[j], dp[i - 1, j - 1])
            m = max(x, y) if x < 0 and y < 0 else max(x, 0) + max(y, 0)
            dp[i, j] = max(dp[i - 1, j], dp[i, j - 1], m)
        return dp[len(nums1) - 1, len(nums2) - 1]
