class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        (N, M) = (len(nums1), len(nums2))
        dp = [[None] * M for _ in range(N)]

        def solve(i, j):
            if i >= N or j >= M:
                return 0
            if dp[i][j] is None:
                dp[i][j] = max(nums1[i] * nums2[j] + solve(i + 1, j + 1), solve(i + 1, j), solve(i, j + 1), solve(i + 1, j + 1))
            return dp[i][j]
        result = solve(0, 0)
        if result == 0 and 0 not in nums1 + nums2:
            if nums1[0] < 0:
                return max(nums1) * min(nums2)
            else:
                return min(nums1) * max(nums2)
        else:
            return result
