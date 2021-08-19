from collections import defaultdict


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        n1_squares = defaultdict(int)
        n2_squares = defaultdict(int)
        for num1 in nums1:
            n1_squares[num1 * num1] += 1
            pass
        for num2 in nums2:
            n2_squares[num2 * num2] += 1
            pass
        triplets = 0
        for i in range(n1 - 1):
            for j in range(i + 1, n1):
                sq = nums1[i] * nums1[j]
                triplets += n2_squares[sq]
        for i in range(n2 - 1):
            for j in range(i + 1, n2):
                sq = nums2[i] * nums2[j]
                triplets += n1_squares[sq]
        return triplets
