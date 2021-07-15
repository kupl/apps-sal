from functools import lru_cache
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find(target, arr):
            seen = Counter()
            count = 0
            for a in arr:
                if target % a == 0:
                    count += seen[target // a]
                seen[a] += 1
            return count

        @lru_cache(None)
        def twoProduct1(target):
            return find(target, nums1)

        @lru_cache(None)
        def twoProduct2(target):
            return find(target, nums2)

        return sum(twoProduct2(a * a) for a in nums1) + sum(twoProduct1(a * a) for a in nums2)
