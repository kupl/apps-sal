import math


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def isSquare(n):
            return math.sqrt(n) == int(math.sqrt(n))
        from collections import Counter
        hash1 = Counter(nums1)
        print(hash1)
        out = 0

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                k = nums2[i] * nums2[j]
                if isSquare(k):
                    if int(math.sqrt(k)) in hash1:
                        out += hash1[int(math.sqrt(k))]
        print(out)
        hash2 = Counter(nums2)

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                k = nums1[i] * nums1[j]
                if isSquare(k):
                    if int(math.sqrt(k)) in hash2:
                        out += hash2[int(math.sqrt(k))]
        print(out)
        return out
