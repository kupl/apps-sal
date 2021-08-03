from typing import List
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        A = Counter([nums1[i]**2 for i in range(len(nums1))])
        B = Counter([nums2[i]**2 for i in range(len(nums2))])
        cnt = 0
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                cnt += A.get(nums2[j] * nums2[k], 0)
        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                cnt += B.get(nums1[j] * nums1[k], 0)
        return cnt
