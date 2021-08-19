from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        ret = 0
        for (k1, v1) in counter1.items():
            for (k2, v2) in counter2.items():
                if k1 * k1 / k2 in counter2:
                    if k2 == k1:
                        ret += v1 * v2 * (v2 - 1)
                    else:
                        ret += v1 * v2 * counter2[k1 * k1 / k2]
        for (k2, v2) in counter2.items():
            for (k1, v1) in counter1.items():
                if k2 * k2 / k1 in counter1:
                    if k2 == k1:
                        ret += v2 * v1 * (v1 - 1)
                    else:
                        ret += v1 * v2 * counter1[k2 * k2 / k1]
        return int(ret / 2)
