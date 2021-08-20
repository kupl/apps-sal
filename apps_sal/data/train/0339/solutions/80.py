import itertools


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dicA = {}
        dicB = {}
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in dicA:
                    dicA[nums1[i] * nums1[j]] += 1
                else:
                    dicA[nums1[i] * nums1[j]] = 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in dicB:
                    dicB[nums2[i] * nums2[j]] += 1
                else:
                    dicB[nums2[i] * nums2[j]] = 1
        ans = 0
        for i in range(len(nums1)):
            try:
                val = dicB[nums1[i] * nums1[i]]
                ans += val
            except KeyError:
                pass
        for i in range(len(nums2)):
            try:
                val = dicA[nums2[i] * nums2[i]]
                ans += val
            except KeyError:
                pass
        return ans
