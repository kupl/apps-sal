class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        ans, a, b = 0, 0, 0
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                ans += max(a, b) + nums1[i]
                i += 1
                j += 1
                a, b = 0, 0
            elif nums1[i] < nums2[j]:
                a += nums1[i]
                i += 1
            else:
                b += nums2[j]
                j += 1
        while i < n1:
            a += nums1[i]
            i += 1
        while j < n2:
            b += nums2[j]
            j += 1
        ans += max(a, b)
        return ans % (10**9 + 7)
