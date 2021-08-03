class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i1, i2, n1, n2, f1, f2 = 0, 0, len(nums1), len(nums2), 0, 0
        while i1 < n1 or i2 < n2:
            if i1 == n1:
                f2 += sum(nums2[i2:])
                i2 = n2
                continue
            if i2 == n2:
                f1 += sum(nums1[i1:])
                i1 = n1
                continue
            if nums1[i1] < nums2[i2]:
                f1 += nums1[i1]
                i1 += 1
                continue
            if nums1[i1] > nums2[i2]:
                f2 += nums2[i2]
                i2 += 1
                continue
            f1 = f2 = max(f2 + nums2[i2], f1 + nums1[i1])
            i1 += 1
            i2 += 1
        return max(f1, f2) % 1000000007
