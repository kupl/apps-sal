class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(nums1, nums2):
            res = 0
            for num in nums1:
                val = num ** 2
                dic = collections.defaultdict(int)
                for e in nums2:
                    res += dic[e]
                    dic[val / e] += 1
            return res
        return helper(nums1, nums2) + helper(nums2, nums1)
