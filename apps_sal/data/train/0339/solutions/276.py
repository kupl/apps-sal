class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.helper(nums1, nums2) + self.helper(nums2, nums1)

    def helper(self, nums1, nums2):
        res = 0
        for n in nums1:
            cnt = {}
            for m in nums2:
                q, d = n * n % m, n * n // m
                if q == 0 and d > 0:
                    if d in cnt:
                        res += cnt[d]
                    cnt[m] = cnt.get(m, 0) + 1
        return res
