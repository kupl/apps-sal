from collections import Counter
from typing import List


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        l1 = len(nums1)
        l2 = len(nums2)
        c1 = Counter()
        c2 = Counter()
        for j in range(l1):
            for k in range(j + 1, l1):
                c1[nums1[j] * nums1[k]] += 1
        for j in range(l2):
            for k in range(j + 1, l2):
                c2[nums2[j] * nums2[k]] += 1
        for i in range(l1):
            res += c2[nums1[i] * nums1[i]]
        for i in range(l2):
            res += c1[nums2[i] * nums2[i]]
        return res
