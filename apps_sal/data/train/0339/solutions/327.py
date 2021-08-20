from itertools import combinations


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (sq1, sq2) = ([num ** 2 for num in nums1], [num ** 2 for num in nums2])
        (prod1, prod2) = ([combo[0] * combo[1] for combo in combinations(nums1, 2)], [combo[0] * combo[1] for combo in combinations(nums2, 2)])
        result = 0
        for sq in set(sq1):
            result += sq1.count(sq) * prod2.count(sq)
        for sq in set(sq2):
            result += sq2.count(sq) * prod1.count(sq)
        return result
