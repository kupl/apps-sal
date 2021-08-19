class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for ele in nums1:
            res += self.twoProduct(ele * ele, nums2)
        for ele in nums2:
            res += self.twoProduct(ele * ele, nums1)
        return res

    def twoProduct(self, prod, nums):
        d = {}
        n = len(nums)
        res = 0
        for i in range(n):
            if prod % nums[i] == 0 and prod // nums[i] in d:
                res += d[prod // nums[i]]
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        return res
