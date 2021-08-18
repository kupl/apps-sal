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
