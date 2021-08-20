class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = collections.defaultdict(lambda: 0)
        m2 = collections.defaultdict(lambda: 0)
        for i in range(len(nums1)):
            m1[nums1[i] ** 2] += 1
        for i in range(len(nums2)):
            m2[nums2[i] ** 2] += 1
        ans = 0
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                ans += m2[nums1[i] * nums1[j]]
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                ans += m1[nums2[i] * nums2[j]]
        return ans
