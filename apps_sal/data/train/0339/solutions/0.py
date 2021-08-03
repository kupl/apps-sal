class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def triplets(nums1, nums2):
            sq = collections.Counter(x * x for x in nums1)
            num = collections.Counter(nums2)

            res = 0
            keys = sorted(num.keys())
            for j, x in enumerate(keys):
                if num[x] > 1 and x * x in sq:
                    res += num[x] * (num[x] - 1) // 2 * sq[x * x]
                for y in keys[j + 1:]:
                    if x * y in sq:
                        res += num[x] * num[y] * sq[x * y]
            return res

        return triplets(nums1, nums2) + triplets(nums2, nums1)
