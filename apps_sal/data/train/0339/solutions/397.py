from collections import defaultdict


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (cnt1, cnt2) = (defaultdict(int), defaultdict(int))
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                cnt1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                cnt2[nums2[i] * nums2[j]] += 1
        ans = 0
        for i in nums1:
            ans += cnt2[i * i]
        for i in nums2:
            ans += cnt1[i * i]
        return ans
