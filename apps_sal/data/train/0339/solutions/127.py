class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter
        C1 = Counter()
        C2 = Counter()
        for num in nums1:
            C1[num * num] += 1
        for num in nums2:
            C2[num * num] += 1
        res = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += C2[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += C1[nums2[i] * nums2[j]]
        return res
