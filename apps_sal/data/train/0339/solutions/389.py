class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sqr_nums1 = defaultdict(int)
        sqr_nums2 = defaultdict(int)
        res = 0
        for x in nums1:
            sqr_nums1[x * x] += 1
        for x in nums2:
            sqr_nums2[x * x] += 1
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += sqr_nums2[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += sqr_nums1[nums2[i] * nums2[j]]
        return res
