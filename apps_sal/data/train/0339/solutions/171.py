from collections import Counter
from itertools import combinations


class Solution:

    def numTriplets(self, nums1, nums2) -> int:
        c_nums1 = Counter(nums1)
        c_nums2 = Counter(nums2)
        res = 0
        self_product1 = Counter()
        cross_product1 = Counter()
        self_product2 = Counter()
        cross_product2 = Counter()
        for (k, v) in c_nums1.items():
            self_product1[k ** 2] += v * (v - 1) // 2
        for (k, v) in c_nums2.items():
            self_product2[k ** 2] += v * (v - 1) // 2
        for comb in combinations(c_nums1.keys(), 2):
            (p, v) = comb
            cross_product1[p * v] += c_nums1[p] * c_nums1[v]
        for comb in combinations(c_nums2.keys(), 2):
            (p, v) = comb
            cross_product2[p * v] += c_nums2[p] * c_nums2[v]
        for (k, v) in c_nums1.items():
            target = k ** 2
            if target in cross_product2:
                res += v * cross_product2[target]
            if target in self_product2:
                res += v * self_product2[target]
        for (k, v) in c_nums2.items():
            target = k ** 2
            if target in cross_product1:
                res += v * cross_product1[target]
            if target in self_product1:
                res += v * self_product1[target]
        return res
