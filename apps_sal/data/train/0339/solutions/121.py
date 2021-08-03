from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for num in nums1:
            res += self.two_product(num ** 2, nums2)
        for num in nums2:
            res += self.two_product(num ** 2, nums1)
        return res

    def two_product(self, target, nums):
        dic, res = defaultdict(int), 0
        for i, num in enumerate(nums):
            if target % num:
                continue
            remain = target // num
            res += dic[remain]
            dic[num] += 1
        return res
