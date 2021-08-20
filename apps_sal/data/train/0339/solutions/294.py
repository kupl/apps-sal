class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        r = 0
        c = Counter()
        for i in nums1:
            if i in c:
                r += c[i]
            for j in nums2:
                c[j * j / i] += 1
        c = Counter()
        for i in nums2:
            if i in c:
                r += c[i]
            for j in nums1:
                c[j * j / i] += 1
        return r
