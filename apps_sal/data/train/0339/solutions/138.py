class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        jk_1 = {}
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if i != j:
                    t = nums1[i] * nums1[j]
                    if t in jk_1:
                        jk_1[t] += 1
                    else:
                        jk_1[t] = 1
        jk_2 = {}
        for i in range(len(nums2)):
            for j in range(len(nums2)):
                if i != j:
                    t = nums2[i] * nums2[j]
                    if t in jk_2:
                        jk_2[t] += 1
                    else:
                        jk_2[t] = 1
        c = 0
        for x in nums1:
            if x * x in jk_2:
                c += jk_2[x * x]
        for x in nums2:
            if x * x in jk_1:
                c += jk_1[x * x]
        return c // 2
