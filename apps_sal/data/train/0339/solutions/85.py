class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (lookup1, lookup2) = (collections.defaultdict(int), collections.defaultdict(int))
        for n in nums1:
            lookup1[n] += 1
        for n in nums2:
            lookup2[n] += 1
        res = 0
        for k in [0, 1]:
            nums = nums1 if not k else nums2
            lookup = lookup1 if k else lookup2
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    prod = nums[i] * nums[j]
                    k = int(math.sqrt(prod))
                    if k * k == prod and k in lookup:
                        res += lookup[k]
        return res
