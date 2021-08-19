class Solution:

    def find(self, n1, n2, c1):
        res = 0
        for j in range(len(n2)):
            for k in range(j + 1, len(n2)):
                t = n2[j] * n2[k]
                sqrt = t ** 0.5
                if sqrt ** 2 != t:
                    continue
                try:
                    i = c1[sqrt]
                except KeyError:
                    i = 0
                res += i
        return res

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n1 = set(nums1)
        n2 = set(nums2)
        c1 = {}
        c2 = {}
        for x in nums1:
            try:
                c1[x] += 1
            except KeyError:
                c1[x] = 1
        for x in nums2:
            try:
                c2[x] += 1
            except KeyError:
                c2[x] = 1
        res += self.find(nums1, nums2, c1)
        res += self.find(nums2, nums1, c2)
        return res
