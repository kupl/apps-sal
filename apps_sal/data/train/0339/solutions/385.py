class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        ans = 0

        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                ans += d2[nums1[i] * nums1[j]]

        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                ans += d1[nums2[i] * nums2[j]]

        return ans
