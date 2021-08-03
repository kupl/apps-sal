# Similar to twoSum problem.
# Let's consider how we can find if value a ** 2 exists as a product of any
#   two elements in array [x, y, ..., z]
# We can store in a set the value of a ** 2 / x for all x in array when fully divisible
# If the next value in array exists in in set, then we found a match
# The time complexity for finding one given value is O(N)
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        for num in nums1:
            res += self.twoProduct(num * num, nums2)

        for num in nums2:
            res += self.twoProduct(num * num, nums1)

        return res

    def twoProduct(self, val, nums):
        prod, res = defaultdict(int), 0
        for num in nums:
            res += prod[num]

            q, r = divmod(val, num)
            if r == 0:
                prod[q] += 1

        return res
