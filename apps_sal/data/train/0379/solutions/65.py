class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        M = 1000000007
        dp1 = [0] * (n1 + 1)
        dp2 = [0] * (n2 + 1)
        i1 = i2 = 0
        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                dp1[i1 + 1] = dp1[i1] + nums1[i1]
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                dp2[i2 + 1] = dp2[i2] + nums2[i2]
                i2 += 1
            else:
                dp1[i1 + 1] = dp2[i2 + 1] = max(dp1[i1] + nums1[i1], dp2[i2] + nums2[i2])
                i1 += 1
                i2 += 1
        while i1 < n1:
            dp1[i1 + 1] = dp1[i1] + nums1[i1]
            i1 += 1
        while i2 < n2:
            dp2[i2 + 1] = dp2[i2] + nums2[i2]
            i2 += 1
        return max(dp1[n1], dp2[n2]) % M
