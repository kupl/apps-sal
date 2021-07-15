from collections import Counter
from itertools import combinations
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            cnt = Counter()
            for a, b in combinations(nums1, 2):
                cnt[a * b] += 1
            return sum(cnt[x * x] for x in nums2)
        return helper(nums1, nums2) + helper(nums2, nums1)
