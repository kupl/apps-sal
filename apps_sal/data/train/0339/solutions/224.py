class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for n in nums1:
            n2 = n * n
            seen = collections.defaultdict(int)
            for i in range(len(nums2)):
                ans += seen[n2 / nums2[i]]
                seen[nums2[i]] += 1
        for n in nums2:
            n2 = n * n
            seen = collections.defaultdict(int)
            for i in range(len(nums1)):
                ans += seen[n2 / nums1[i]]
                seen[nums1[i]] += 1
        return ans
