class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def two(target, nums):
            counter = collections.defaultdict(int)
            res = 0
            for num in nums:
                if target % num == 0:
                    res += counter[target // num]
                counter[num] += 1
            return res

        res = 0
        for num in nums1:
            res += two(num * num, nums2)
        for num in nums2:
            res += two(num * num, nums1)

        return res
