class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        res += sum((self.get_target_products(n * n, nums2) for n in nums1))
        res += sum((self.get_target_products(n * n, nums1) for n in nums2))
        return res

    def get_target_products(self, target, nums):
        d = collections.Counter()
        res = 0
        for i in range(len(nums)):
            if target / nums[i] in d:
                res += d[target / nums[i]]
            d[nums[i]] += 1
        return res
