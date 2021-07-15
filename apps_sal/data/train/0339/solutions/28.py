class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        d1 = collections.defaultdict(int)
        for j in range(N1):
            for k in range(j + 1, N1):
                d1[nums1[j] * nums1[k]] += 1
        d2 = collections.defaultdict(int)
        for j in range(N2):
            for k in range(j + 1, N2):
                d2[nums2[j] * nums2[k]] += 1
        ans = 0
        for i in range(N1):
            ans += d2[nums1[i] * nums1[i]]
        for i in range(N2):
            ans += d1[nums2[i] * nums2[i]]
        return ans
