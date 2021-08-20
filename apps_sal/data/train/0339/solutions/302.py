class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(alist, blist):
            res = 0
            for a in alist:
                bset = collections.Counter()
                a2 = a * a
                for b in blist:
                    if a2 / b in bset:
                        res += bset[a2 / b]
                    bset[b] += 1
            return res
        return helper(nums1, nums2) + helper(nums2, nums1)
