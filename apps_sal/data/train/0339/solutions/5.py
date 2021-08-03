from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = Counter([x * x for x in nums1]), Counter([x * x for x in nums2])
        count = 0
        l1, l2 = len(nums1), len(nums2)
        for i in range(l2 - 1):
            for j in range(i + 1, l2):
                count += n1[nums2[i] * nums2[j]]
        for i in range(l1 - 1):
            for j in range(i + 1, l1):
                count += n2[nums1[i] * nums1[j]]

        return count
