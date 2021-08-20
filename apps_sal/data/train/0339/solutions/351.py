class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for n in nums1:
            d = {}
            for (i, m) in enumerate(nums2):
                if n ** 2 / m in d:
                    ans += d[n ** 2 / m]
                if m in d:
                    d[m] += 1
                else:
                    d[m] = 1
        for n in nums2:
            d = {}
            for (i, m) in enumerate(nums1):
                if n ** 2 / m in d:
                    ans += d[n ** 2 / m]
                if m in d:
                    d[m] += 1
                else:
                    d[m] = 1
        return ans
