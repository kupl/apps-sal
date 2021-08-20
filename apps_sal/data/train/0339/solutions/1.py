class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        nums1 = sorted(count1.keys())
        nums2 = sorted(count2.keys())
        tot = 0
        for (c1, n1, c2, n2) in [(count1, nums1, count2, nums2), (count2, nums2, count1, nums1)]:
            for a in n1:
                s = a ** 2
                for b in n2:
                    if b > a:
                        break
                    if s % b == 0 and s // b in c2:
                        print((a, b))
                        if b == a:
                            if c2[b] >= 2:
                                tot += c1[a] * comb(c2[b], 2)
                        else:
                            tot += c1[a] * c2[b] * c2[s // b]
        return tot
