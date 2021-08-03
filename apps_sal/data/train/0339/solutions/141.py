class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        res = 0
        for n1 in nums1:
            x = n1 ** 2
            for n2 in nums2:
                if x % n2 == 0 and (x // n2) in c2:
                    if x // n2 == n2:
                        res += c2[x // n2] - 1
                    else:
                        res += c2[x // n2]
        for n2 in nums2:
            x = n2 ** 2
            for n1 in nums1:
                if x % n1 == 0 and (x // n1) in c1:
                    if x // n1 == n1:
                        res += c1[x // n1] - 1
                    else:
                        res += c1[x // n1]
        return res // 2
