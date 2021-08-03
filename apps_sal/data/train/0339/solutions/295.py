from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1 = defaultdict(list)
        pd1 = defaultdict(list)
        sq2 = defaultdict(list)
        pd2 = defaultdict(list)

        for i in range(0, len(nums1)):
            n1 = nums1[i]
            sq1[n1 * n1].append(i)
            for j in range(i + 1, len(nums1)):
                n2 = nums1[j]
                pd1[n1 * n2].append([i, j])

        for i in range(0, len(nums2)):
            n1 = nums2[i]
            sq2[n1 * n1].append(i)
            for j in range(i + 1, len(nums2)):
                n2 = nums2[j]
                pd2[n1 * n2].append([i, j])

        type1 = 0
        type2 = 0

        for sq in sq1:
            if sq in pd2:
                type1 += (len(sq1[sq]) * len(pd2[sq]))
        for sq in sq2:
            if sq in pd1:
                type2 += (len(sq2[sq]) * len(pd1[sq]))
        return type1 + type2
