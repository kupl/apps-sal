from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        h1 = defaultdict(list)
        h2 = defaultdict(list)
        n = len(nums1)
        m = len(nums2)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                h1[nums1[i] * nums1[j]].append((i, j))
        for i in range(m):
            for j in range(i + 1, m):
                h2[nums2[i] * nums2[j]].append((i, j))
        for i in range(n):
            if nums1[i]**2 in h2:
                ans += len(h2[nums1[i]**2])
        for i in range(m):
            if nums2[i]**2 in h1:
                ans += len(h1[nums2[i]**2])
        return ans
