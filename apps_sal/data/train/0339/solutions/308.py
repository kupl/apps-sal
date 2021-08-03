from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0

        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for x in nums1:
            h1[x] += 1
        for x in nums2:
            h2[x] += 1

        for x in nums1:
            for y in nums2:
                if x * x / y != x * x // y:
                    continue
                key = x * x // y
                if h2[key] > 0:
                    if key == y:
                        ret += h2[key] - 1
                    else:
                        ret += h2[key]

        for x in nums2:
            for y in nums1:
                if x * x / y != x * x // y:
                    continue
                key = x * x // y
                if h1[key] > 0:
                    if key == y:
                        ret += h1[key] - 1
                    else:
                        ret += h1[key]

        return ret // 2
