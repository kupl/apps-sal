class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def tow_product(A, target):

            d = {}
            res = 0
            for x in A:
                if target % x == 0 and target // x in d:
                    res += d[target // x]
                d[x] = d.get(x, 0) + 1
            return res

        def count(nums1, nums2):
            res = 0
            last_cnt = 0
            for i in range(len(nums1)):
                if i > 0 and nums1[i] == nums1[i - 1]:
                    res += last_cnt
                else:
                    last_cnt = tow_product(nums2, nums1[i]**2)
                    res += last_cnt
            return res

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        return count(nums1, nums2) + count(nums2, nums1)
