class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1

        ans = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                x = nums1[i] * nums1[j]
                ans += d2[x]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                x = nums2[i] * nums2[j]
                ans += d1[x]
        return ans
