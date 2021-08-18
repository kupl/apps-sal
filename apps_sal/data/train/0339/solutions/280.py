class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProduct(n, nums):
            counter = collections.Counter()
            res = 0
            for num in nums:
                if n % num == 0:
                    res += counter[n / num]
                counter[num] += 1
            return res
        res = 0
        for num in nums1:
            res += twoProduct(num * num, nums2)
        for num in nums2:
            res += twoProduct(num * num, nums1)
        return res
