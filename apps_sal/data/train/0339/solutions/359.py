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

        def twoProduct(target, nums):
            if target in lut:
                return lut[target]
            lut[target] = find(target, nums)
            return lut[target]
        lut = Counter()
        ret1 = sum((twoProduct(a * a, nums2) for a in nums1))
        lut = Counter()
        ret2 = sum((twoProduct(a * a, nums1) for a in nums2))
        return ret1 + ret2
