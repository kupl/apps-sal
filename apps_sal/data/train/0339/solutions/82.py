import collections


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counts1 = collections.Counter(nums1)
        counts2 = collections.Counter(nums2)
        print(counts1)
        print(counts2)

        def doit(c1, c2):
            total = 0
            for k1 in c1:
                for k2 in c2:
                    neededK = (k1 * k1) / k2
                    if neededK == int(neededK):
                        neededK = int(neededK)
                        if k2 == neededK:
                            i = c2[neededK]
                            j = (i - 1 + 1) * (i - 1) // 2
                            total += c1[k1] * j
                        elif k2 < neededK:
                            total += c1[k1] * c2[k2] * c2[neededK]
                        print(k1, k2, neededK, total)
            return total

        return doit(counts1, counts2) + doit(counts2, counts1)
