class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter
        m, n = len(nums1), len(nums2)
        res = 0

        pool2 = Counter()
        for i in range(n - 1):
            for j in range(i + 1, n):
                curr = nums2[i] * nums2[j]
                pool2[curr] += 1

        for v in nums1:
            curr = v ** 2
            if curr in pool2:
                res += pool2[curr]

        pool1 = Counter()
        for i in range(m - 1):
            for j in range(i + 1, m):
                curr = nums1[i] * nums1[j]
                pool1[curr] += 1

        for v in nums2:
            curr = v ** 2
            if curr in pool1:
                res += pool1[curr]

        return res
