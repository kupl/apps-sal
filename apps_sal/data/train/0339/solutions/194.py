class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        res = 0
        for x in nums1:
            t = x * x
            m = {}
            for y in nums2:
                if t % y == 0:
                    res += m.get(t // y, 0)
                m[y] = m.get(y, 0) + 1

        for y in nums2:
            t = y * y
            m = {}
            for x in nums1:
                if t % x == 0:
                    res += m.get(t // x, 0)
                m[x] = m.get(x, 0) + 1

        return res
