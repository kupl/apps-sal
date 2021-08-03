from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        self.res = 0

        def count(a1, a2):
            for e1 in [e * e for e in a1]:
                m = defaultdict(int)
                for e2 in a2:
                    if e1 % e2 == 0:
                        self.res += m[e1 // e2]
                    m[e2] += 1

        count(nums1, nums2)
        count(nums2, nums1)

        return self.res
