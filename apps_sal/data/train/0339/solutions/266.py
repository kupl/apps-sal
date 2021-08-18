from collections import Counter
from itertools import combinations
from math import sqrt


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        count1 = Counter(nums1)
        count2 = Counter(nums2)
        set1 = set(nums1)
        set2 = set(nums2)
        nums11 = list([x * x for x in set1])
        nums22 = list([x * x for x in set2])
        count = 0
        for i, j in list(combinations(set1, 2)):
            if i * j in nums22:
                count += count2[sqrt(i * j)] * count1[i] * count1[j]
        for i, j in list(combinations(set2, 2)):
            if i * j in nums11:
                count += count1[sqrt(i * j)] * count2[i] * count2[j]
        for i in set1:
            if count1[i] > 1 and i * i in nums22:
                count += count1[i] * (count1[i] - 1) * count2[i] // 2
        for i in set2:
            if count2[i] > 1 and i * i in nums11:
                count += count2[i] * (count2[i] - 1) * count1[i] // 2
        return count
