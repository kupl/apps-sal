from collections import defaultdict


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for n in nums1:
            d1[n * n] += 1
        for n in nums2:
            d2[n * n] += 1
        count = 0
        for i in range(0, len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                count += d2[nums1[i] * nums1[j]]
        for i in range(0, len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                count += d1[nums2[i] * nums2[j]]
        return count
