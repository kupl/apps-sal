class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        set1 = collections.Counter([x * x for x in nums1])
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                ans += set1[nums2[i] * nums2[j]]
        set2 = collections.Counter([x * x for x in nums2])
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                ans += set2[nums1[i] * nums1[j]]

        return ans
