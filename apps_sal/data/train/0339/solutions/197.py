from collections import defaultdict as dt


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = 0
        for x in nums1:
            d = dt(int)
            for y in nums2:
                if x * x % y == 0 and x * x // y in d:
                    cnt += d[x * x // y]
                d[y] += 1
        for x in nums2:
            d = dt(int)
            for y in nums1:
                if x * x % y == 0 and x * x // y in d:
                    cnt += d[x * x // y]
                d[y] += 1
        return cnt
