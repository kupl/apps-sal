class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        nums1prod = [[nums1[i] * nums1[j] for i in range(n)] for j in range(n)]
        nums2prod = [[nums2[i] * nums2[j] for i in range(m)] for j in range(m)]
        nums1sq = [x**2 for x in nums1]
        nums2sq = [x**2 for x in nums2]

        hm1sq = Counter(nums1sq)
        hm2sq = Counter(nums2sq)

        trip = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums1prod[i][j] in hm2sq:
                    trip += hm2sq[nums1prod[i][j]]

        for i in range(m):
            for j in range(i + 1, m):
                if nums2prod[i][j] in hm1sq:
                    trip += hm1sq[nums2prod[i][j]]

        return trip
