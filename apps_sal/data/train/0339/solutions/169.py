from itertools import combinations
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num1Sq = [i * i for i in nums1]
        num2Sq = [i * i for i in nums2]
        c1 = Counter(num1Sq)
        c2 = Counter(num2Sq)

        comb1 = list(combinations(nums1, 2))
        comb2 = list(combinations(nums2, 2))

        res = 0

        for i in comb1:
            res += c2[i[0] * i[1]]

        for i in comb2:
            res += c1[i[0] * i[1]]

        return res
