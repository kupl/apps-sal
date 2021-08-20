class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (i, j, n, m) = (0, 0, len(nums1), len(nums2))
        (a, b) = (0, 0)
        result = 0
        while i < n or j < m:
            if i < n and (j == m or nums1[i] < nums2[j]):
                a += nums1[i]
                i += 1
            elif j < m and (i == n or nums1[i] > nums2[j]):
                b += nums2[j]
                j += 1
            else:
                a = b = max(a, b) + nums1[i]
                i += 1
                j += 1
        return max(a, b) % (10 ** 9 + 7)
