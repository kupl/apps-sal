from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (mul1, mul2) = (Counter(), Counter())
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                mul1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                mul2[nums2[i] * nums2[j]] += 1
        tots = 0
        for i in range(len(nums1)):
            tots += mul2[nums1[i] ** 2]
        for i in range(len(nums2)):
            tots += mul1[nums2[i] ** 2]
        return tots
