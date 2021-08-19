class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(a, b):
            res = 0
            for num in a:
                tar = num ** 2
                cnt = collections.defaultdict(int)
                for x in b:
                    res += cnt[tar / x]
                    cnt[x] += 1
            return res
        return helper(nums1, nums2) + helper(nums2, nums1)
