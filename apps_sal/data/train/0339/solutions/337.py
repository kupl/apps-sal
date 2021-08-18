class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_squared = [i**2 for i in nums1]
        nums2_squared = [i**2 for i in nums2]

        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)

        res = 0
        for n1 in nums1:
            for target in nums2_squared:
                if target / n1 in c1:
                    res += c1[target / n1]
                    if n1**2 == target:
                        res -= 1

        for n2 in nums2:
            for target in nums1_squared:
                if target / n2 in c2:
                    res += c2[target / n2]
                    if n2**2 == target:
                        res -= 1

        return res // 2
