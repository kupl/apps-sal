class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = {}, {}
        for v in nums1:
            d1[v * v] = d1.get(v * v, 0) + 1
        for v in nums2:
            d2[v * v] = d2.get(v * v, 0) + 1
        res = 0
        for i, v in enumerate(nums1):
            for j in range(i + 1, len(nums1)):
                res += d2.get(v * nums1[j], 0)
        for i, v in enumerate(nums2):
            for j in range(i + 1, len(nums2)):
                res += d1.get(v * nums2[j], 0)
        return res
