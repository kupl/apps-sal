class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        s1 = collections.Counter()
        for n1 in nums1:
            s2 = collections.Counter()
            for n2 in nums2:
                if n1 * n1 % n2 == 0 and n1 * n1 // n2 in s2:
                    res += s2[n1 * n1 // n2]
                if n2 * n2 % n1 == 0 and n2 * n2 // n1 in s1:
                    res += s1[n2 * n2 // n1]
                s2[n2] += 1
            s1[n1] += 1
        return res
