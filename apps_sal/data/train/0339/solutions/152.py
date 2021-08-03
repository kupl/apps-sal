from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for i in nums1:
            for j in nums2:
                j2 = j * j
                ji = j2 // i
                if ji * i == j2:
                    res += c1[j2 // i]
                    if ji == i:
                        res -= 1
                i2 = i * i
                ij = i2 // j
                if ij * j == i2:
                    res += c2[i2 // j]
                    if ij == j:
                        res -= 1
        return res // 2
