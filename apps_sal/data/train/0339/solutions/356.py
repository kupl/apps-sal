class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)

        res = 0
        for x in c1:
            for y in c2:
                if x == y:
                    res += (c1[x] * c2[y] * (c2[y] - 1)) // 2
                elif x**2 % y == 0 and y < x**2 // y:
                    res += c1[x] * c2[y] * c2[x**2 // y]

        c1, c2 = c2, c1
        for x in c1:
            for y in c2:
                if x == y:
                    res += (c1[x] * c2[y] * (c2[y] - 1)) // 2
                elif x**2 % y == 0 and y < x**2 // y:
                    res += c1[x] * c2[y] * c2[x**2 // y]

        return res
