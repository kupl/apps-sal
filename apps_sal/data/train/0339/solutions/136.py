class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getProd(nums):
            dict1 = {}
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        prod = nums[i] * nums[j]
                        if prod not in dict1:
                            dict1[prod] = 0
                        dict1[prod] += 1
            return dict1
        res = 0
        d1 = getProd(nums1)
        for x in nums2:
            if x**2 in d1:
                res += d1[x**2]
        d2 = getProd(nums2)
        for x in nums1:
            if x**2 in d2:
                res += d2[x**2]
        return res//2
