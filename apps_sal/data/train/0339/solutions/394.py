import collections


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) <= 1 and len(nums2) <= 1:
            return 0
        numTri = 0
        nums1Sq = [num**2 for num in nums1]
        nums2Sq = [num**2 for num in nums2]
        nums1Mul = collections.Counter([nums1[i] * nums1[j] for i in range(len(nums1)) for j in range(i + 1, len(nums1))])
        nums2Mul = collections.Counter([nums2[i] * nums2[j] for i in range(len(nums2)) for j in range(i + 1, len(nums2))])
        for num in nums1Sq:
            if num in nums2Mul:
                numTri += nums2Mul[num]
        for num in nums2Sq:
            if num in nums1Mul:
                numTri += nums1Mul[num]
        return numTri
