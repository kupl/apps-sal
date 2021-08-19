class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (ans, m1, m2) = (0, Counter([x ** 2 for x in nums1]), Counter([x ** 2 for x in nums2]))
        (n1, n2) = (len(nums1), len(nums2))
        for i in range(n1 - 1):
            for j in range(i + 1, n1):
                ans += m2[nums1[i] * nums1[j]]
        for i in range(n2 - 1):
            for j in range(i + 1, n2):
                ans += m1[nums2[i] * nums2[j]]
        return ans
