class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(nums1, nums2):
            res = 0
            for i in nums1:
                map1 = defaultdict(int)
                sq = i ** 2
                for j in nums2:
                    comp = sq / j
                    if j in map1:
                        res += map1[j]
                    map1[comp] += 1
            return res
        return count(nums1, nums2) + count(nums2, nums1)
