from collections import Counter
from math import sqrt


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def is_perfect(x):
            return int(sqrt(x)) ** 2 == x
        (size1, size2) = (len(nums1), len(nums2))
        (count1, count2) = (Counter(nums1), Counter(nums2))
        (max1, max2) = (max(nums1), max(nums2))
        nums1.sort()
        nums2.sort()
        res = 0
        for i in range(size2):
            if nums2[i] > max1:
                break
            for j in range(i + 1, size2):
                mul = nums2[i] * nums2[j]
                if is_perfect(mul):
                    res += count1[int(sqrt(mul))]
        for i in range(size1):
            if nums1[i] > max2:
                break
            for j in range(i + 1, size1):
                mul = nums1[i] * nums1[j]
                if is_perfect(mul):
                    res += count2[int(sqrt(mul))]
        return res
