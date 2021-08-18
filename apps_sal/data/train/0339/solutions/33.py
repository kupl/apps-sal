class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def getRoots(nums):
            prods = []
            for (i, j) in itertools.combinations(nums, 2):
                prods.append(i * j)
            return prods

        def ways(nums1, nums2):
            ans = 0
            square = collections.Counter([n**2 for n in nums1])
            prods = getRoots(nums2)
            for p in prods:
                ans += square[p]
            return ans

        return ways(nums1, nums2) + ways(nums2, nums1)
