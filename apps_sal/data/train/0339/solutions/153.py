class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = {}, {}
        for i in range(len(nums1)):
            for j in range(i):
                d1[nums1[i] * nums1[j]] = d1.get(nums1[i] * nums1[j], 0) + 1
        for i in range(len(nums2)):
            for j in range(i):
                d2[nums2[i] * nums2[j]] = d2.get(nums2[i] * nums2[j], 0) + 1

        return sum(d1.get(i * i, 0) for i in nums2) + sum(d2.get(j * j, 0) for j in nums1)
