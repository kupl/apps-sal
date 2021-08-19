class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dp = collections.defaultdict(int)
        i, j = len(nums1) - 2, len(nums2) - 2
        dp[nums1[-1]] = nums1[-1]
        dp[nums2[-1]] = nums2[-1]
        while i >= 0 or j >= 0:
            v1, v2 = nums1[i] if i >= 0 else -1, nums2[j] if j >= 0 else -1
            # print(i,j,v1,v2,dp)
            if v1 > v2:
                dp[v1] = v1 + dp[nums1[i + 1]]
                i -= 1
            elif v1 < v2:
                dp[v2] = v2 + dp[nums2[j + 1]]
                j -= 1
            else:
                dp[v1] = v1 + max(dp[nums1[i + 1]], dp[nums2[j + 1]])
                i -= 1
                j -= 1
        return max(dp[nums1[0]], dp[nums2[0]]) % 1000000007
