class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        (double1, double2) = (collections.Counter(), collections.Counter())
        for n in nums1:
            double1[n * n] += 1
        for n in nums2:
            double2[n * n] += 1
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in double2:
                    res += double2[nums1[i] * nums1[j]]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in double1:
                    res += double1[nums2[i] * nums2[j]]
        return res
