class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1, dic2 = collections.defaultdict(int), collections.defaultdict(int)

        for num in nums1:
            dic1[num**2] += 1
        for num in nums2:
            dic2[num**2] += 1

        res = 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                res += dic2[nums1[i] * nums1[j]]

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                res += dic1[nums2[i] * nums2[j]]

        return res
