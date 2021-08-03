class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        dic1 = {}
        dic2 = {}
        for i, e in enumerate(nums1):
            target = e ** 2
            for j in range(len(nums2)):
                if target % nums2[j] == 0:
                    if nums2[j] in dic1:
                        res += dic1[nums2[j]]
                    dic1[target // nums2[j]] = dic1.get(target // nums2[j], 0) + 1
            dic1 = {}

        for i, e in enumerate(nums2):
            target = e ** 2
            for j in range(len(nums1)):
                if target % nums1[j] == 0:
                    if nums1[j] in dic2:
                        res += dic2[nums1[j]]
                    dic2[target // nums1[j]] = dic2.get(target // nums1[j], 0) + 1
            dic2 = {}

        return res
