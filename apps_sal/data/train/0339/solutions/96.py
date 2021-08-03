class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter

        c1 = Counter()
        c2 = Counter()
        r1 = 0
        r2 = 0
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if i < j:
                    c1[nums1[i] * nums1[j]] += 1

        for i in range(len(nums2)):
            for j in range(len(nums2)):
                if i < j:
                    c2[nums2[i] * nums2[j]] += 1

        for i in nums2:
            r1 += c1[i * i]
        for i in nums1:
            r2 += c2[i * i]

        return r1 + r2
