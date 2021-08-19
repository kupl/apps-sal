class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(l1, l2):
            res = 0
            for i in range(len(l1)):
                comp = dict()
                target = l1[i] ** 2
                for j in range(len(l2)):
                    if target / l2[j] in comp:
                        res += comp[target / l2[j]]
                    comp[l2[j]] = comp.get(l2[j], 0) + 1
            return res
        return helper(nums1, nums2) + helper(nums2, nums1)
