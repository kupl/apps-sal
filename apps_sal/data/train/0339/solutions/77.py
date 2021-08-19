from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        output = 0
        sq1 = Counter(map(lambda q: q * q, nums1))
        sq2 = Counter(map(lambda q: q * q, nums2))
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                output += sq1[nums2[i] * nums2[j]]
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                output += sq2[nums1[i] * nums1[j]]
        return output
