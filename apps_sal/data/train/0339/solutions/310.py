from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        jk1, jk2 = defaultdict(set), defaultdict(set)
        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                jk1[nums1[j] * nums1[k]].add((j, k))
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                jk2[nums2[j] * nums2[k]].add((j, k))

        res = 0
        for i in range(len(nums1)):
            res += len(jk2[nums1[i] ** 2])
        for i in range(len(nums2)):
            res += len(jk1[nums2[i] ** 2])

        return res
