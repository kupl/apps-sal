from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for n in nums1:
            mp1[n * n] += 1
        for n in nums2:
            mp2[n * n] += 1

        products1 = self.products(nums1)
        products2 = self.products(nums2)

        score = 0
        for p in products1:
            if mp2.get(p):
                score += mp2[p]
        for p in products2:
            if mp1.get(p):
                score += mp1[p]

        return score

    def products(self, nums):
        products = []
        n = len(nums)
        for i in range(0, n - 1):
            for m in nums[i + 1:]:
                products.append(nums[i] * m)
        return products
