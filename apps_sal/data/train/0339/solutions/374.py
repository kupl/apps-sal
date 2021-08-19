from collections import Counter
from itertools import combinations


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = Counter([x * y for (x, y) in combinations(nums1, 2)])
        c2 = Counter([x * y for (x, y) in combinations(nums2, 2)])
        return sum([c1[x * x] for x in nums2]) + sum([c2[x * x] for x in nums1])
