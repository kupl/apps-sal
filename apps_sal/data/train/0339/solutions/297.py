from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0

        for n in nums1:
            t = defaultdict(int)
            for m in nums2:
                if (n * n) % m == 0 and ((n * n) // m) in t:
                    count += t[(n * n) // m]
                t[m] += 1

        for n in nums2:
            t = defaultdict(int)
            for m in nums1:
                if (n * n) % m == 0 and ((n * n) // m) in t:
                    count += t[(n * n) // m]
                t[m] += 1

        return count
