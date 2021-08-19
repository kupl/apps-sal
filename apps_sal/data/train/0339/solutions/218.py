class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num12 = [x * x for x in nums1]
        num22 = [x * x for x in nums2]
        ans = 0
        for j2 in num22:
            c2 = Counter()
            for i in nums1:
                if j2 % i == 0:
                    if i in c2:
                        ans += c2[i]
                    c2[j2 // i] += 1
        for j1 in num12:
            c1 = Counter()
            for i in nums2:
                if j1 % i == 0:
                    if i in c1:
                        ans += c1[i]
                    c1[j1 // i] += 1
        return ans
