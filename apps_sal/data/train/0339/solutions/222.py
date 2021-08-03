class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        p1 = {}
        p2 = {}
        c = 0
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if i != j:
                    p1[nums1[i] * nums1[j]] = p1.get(nums1[i] * nums1[j], 0) + 1

        for i in range(len(nums2)):
            for j in range(len(nums2)):
                if i != j:
                    p2[nums2[i] * nums2[j]] = p2.get(nums2[i] * nums2[j], 0) + 1

        for i in nums1:
            if i * i in list(p2.keys()):
                c += p2[i * i] // 2
        for i in nums2:
            if i * i in list(p1.keys()):
                c += p1[i * i] // 2
        return c
