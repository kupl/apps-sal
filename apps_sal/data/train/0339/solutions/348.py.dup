class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = dict(), dict()

        for idx, n1 in enumerate(nums1):
            d1[idx] = dict()
            for elm in nums1[idx + 1:]:
                try:
                    d1[idx][elm] += 1
                except KeyError:
                    d1[idx][elm] = 1

        for idx, n2 in enumerate(nums2):
            d2[idx] = dict()
            for elm in nums2[idx + 1:]:
                try:
                    d2[idx][elm] += 1
                except KeyError:
                    d2[idx][elm] = 1

        good = 0

        for n1 in nums1:
            for idx, n2 in enumerate(nums2):
                try:
                    good += d2[idx][n1**2 / n2]
                except KeyError:
                    pass

        for n2 in nums2:
            for idx, n1 in enumerate(nums1):
                try:
                    good += d1[idx][n2**2 / n1]
                except KeyError:
                    pass

        return good
