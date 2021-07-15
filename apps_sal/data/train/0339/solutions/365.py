from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = 0
        for x in nums1:
            sqr = x*x
            for y in c2.keys():
                if sqr%y == 0:
                    z = sqr//y
                    if y == z:
                        ans += c2[y] * (c2[y]-1)
                    else:
                        ans+= c2[y] * c2.get(z, 0)
        for x in nums2:
            sqr = x*x
            for y in c1.keys():
                if sqr%y == 0:
                    z = sqr//y
                    if y == z:
                        ans += c1[y] * (c1[y]-1)
                    else:
                        ans+= c1[y] * c1.get(z, 0)
        return ans//2
