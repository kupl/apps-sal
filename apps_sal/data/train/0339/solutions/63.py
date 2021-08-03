class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        nums2_pairs = Counter()
        nums1_pairs = Counter()

        for i in range(n):
            for j in range(i + 1, n):
                nums1_pairs[nums1[i] * nums1[j]] += 1

        for i in range(m):
            for j in range(i + 1, m):
                nums2_pairs[nums2[i] * nums2[j]] += 1

        ans = 0
        for i in range(n):
            ans += nums2_pairs[nums1[i] * nums1[i]]
        for i in range(m):
            ans += nums1_pairs[nums2[i] * nums2[i]]
        return ans
