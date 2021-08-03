class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        prod_nums1 = collections.Counter([v1 * v2 for v1, v2 in itertools.combinations(nums1, 2)])
        prod_nums2 = collections.Counter([v1 * v2 for v1, v2 in itertools.combinations(nums2, 2)])

        return sum([prod_nums2[n1**2] for n1 in nums1]) + sum([prod_nums1[n2**2] for n2 in nums2])
