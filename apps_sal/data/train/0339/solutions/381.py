class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # TC : O(n**2), where n = max(#nums1, #nums2)
        nums1_sq_dct = collections.defaultdict(int)
        nums2_sq_dct = collections.defaultdict(int)

        res = 0

        for x in nums1:
            nums1_sq_dct[x**2] += 1
        for y in nums2:
            nums2_sq_dct[y**2] += 1

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                res += nums2_sq_dct[nums1[i] * nums1[j]]

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                res += nums1_sq_dct[nums2[i] * nums2[j]]

        return res
