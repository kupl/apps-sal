class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            target = nums1[i] ** 2
            prev = collections.Counter()
            for j in range(len(nums2)):
                if target % nums2[j] != 0:
                    continue
                val = target // nums2[j]
                if val in prev:
                    res += prev[val]
                prev[nums2[j]] += 1
        for i in range(len(nums2)):
            target = nums2[i] ** 2
            prev = collections.Counter()
            for j in range(len(nums1)):
                if target % nums1[j] != 0:
                    continue
                val = target // nums1[j]
                if val in prev:
                    res += prev[val]
                prev[nums1[j]] += 1
        return res
