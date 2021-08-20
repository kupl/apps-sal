class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def getProd(n1, n2):
            c2 = Counter(n2)
            res = 0
            for x in n1:
                prod = x ** 2
                for n in n2:
                    if prod % n > 0:
                        continue
                    d = prod // n
                    if d in c2:
                        res += c2[d]
                        if d == n:
                            res -= 1
            return res
        r = 0
        r += getProd(nums1, nums2)
        r += getProd(nums2, nums1)
        return r // 2
