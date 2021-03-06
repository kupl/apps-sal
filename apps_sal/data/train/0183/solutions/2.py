class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * (n2 + 1) for j in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                dp[i + 1][j + 1] = max(dp[i][j] + max(0, nums1[i] * nums2[j]), dp[i][j + 1], dp[i + 1][j])
        if dp[-1][-1] != 0:
            return dp[-1][-1]
        nums1.sort()
        nums2.sort()
        a = nums1[0] if nums1[0] > 0 else nums1[-1]
        b = nums2[0] if nums2[0] > 0 else nums2[-1]
        return a * b
