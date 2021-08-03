class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        def f(i, p):

            if (p == 0 and i >= len(nums1)) or (p == 1 and i >= len(nums2)):
                return 0

            if (i, p) in dp:
                return dp[i, p]

            ans = f(i + 1, p)

            if p == 0:
                if nums1[i] in b:
                    ans = max(ans, f(b[nums1[i]] + 1, 1 - p))

            else:
                if nums2[i] in a:
                    ans = max(ans, f(a[nums2[i]] + 1, 1 - p))

            dp[i, p] = ans + (nums1[i] if p == 0 else nums2[i])

            return dp[i, p]

        a, b, dp = {}, {}, {}
        for i, j in enumerate(nums1):
            a[j] = i

        for i, j in enumerate(nums2):
            b[j] = i

        return max(f(0, 0), f(0, 1)) % (10**9 + 7)
