class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def comb(nums, k):
            res = 0
            count = collections.defaultdict(int)
            for i in range(len(nums)):
                x = nums[i]
                y = k * k // x
                if x * y == k * k:
                    res += count[y]
                count[x] += 1
            return res
        res = 0
        for x in nums1:
            res += comb(nums2, x)
        for x in nums2:
            res += comb(nums1, x)
        return res
