class Solution:
    def count(self, nums1: List[int], nums2: List[int]) -> int:
        c = 0
        for n in nums1:
            sq = n ** 2
            counter = Counter()
            for k in nums2:
                if sq % k == 0:
                    c += counter[sq // k]
                counter[k] += 1
        return c

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.count(nums1, nums2) + self.count(nums2, nums1)
