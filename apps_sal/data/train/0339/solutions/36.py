from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = defaultdict(int)
        t2 = defaultdict(int)
        ans = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                t1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                t2[nums2[i] * nums2[j]] += 1

        for n in nums1:
            ans += t2[n * n]
        for n in nums2:
            ans += t1[n * n]
        return ans
