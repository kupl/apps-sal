from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        squares1 = Counter([x ** 2 for x in nums1])
        squares2 = Counter([x ** 2 for x in nums2])
        total = 0
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if (square := (nums2[i] * nums2[j])) in squares1:
                    total += squares1[square]
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if (square := (nums1[i] * nums1[j])) in squares2:
                    total += squares2[square]
        return total
