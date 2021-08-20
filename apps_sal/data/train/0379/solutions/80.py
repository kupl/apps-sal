class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        KMAX = 10 ** 9 + 7
        (i1, i2) = (0, 0)
        (N1, N2) = (len(nums1), len(nums2))
        res = 0
        (total1, total2) = (0, 0)
        while i1 < N1 or i2 < N2:
            if i1 == N1:
                total2 += nums2[i2]
                i2 += 1
                continue
            if i2 == N2:
                total1 += nums1[i1]
                i1 += 1
                continue
            if nums1[i1] == nums2[i2]:
                res += nums1[i1] + max(total1, total2)
                i1 += 1
                i2 += 1
                (total1, total2) = (0, 0)
            elif nums1[i1] < nums2[i2]:
                total1 += nums1[i1]
                i1 += 1
            else:
                total2 += nums2[i2]
                i2 += 1
        res += max(total1, total2)
        return res % KMAX
