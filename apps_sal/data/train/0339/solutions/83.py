class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        lookup1, lookup2, res = {}, {}, 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in lookup1:
                    lookup1[nums1[i] * nums1[j]] += 1
                else:
                    lookup1[nums1[i] * nums1[j]] = 1
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in lookup2:
                    lookup2[nums2[i] * nums2[j]] += 1
                else:
                    lookup2[nums2[i] * nums2[j]] = 1

        for i in nums1:
            if i * i in lookup2:
                res += lookup2[i * i]

        for i in nums2:
            if i * i in lookup1:
                res += lookup1[i * i]
        return res
