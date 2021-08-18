class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        count = 0
        d1 = {}
        d2 = {}

        for i in nums1:
            if i**2 not in d1:
                d1[i**2] = 1
            else:
                d1[i**2] += 1

        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                prod = nums2[j] * nums2[k]
                if prod in d1:
                    count += d1[prod]

        for i in nums2:
            if i**2 not in d2:
                d2[i**2] = 1
            else:
                d2[i**2] += 1

        for j in range(len(nums1)):
            for k in range(j + 1, len(nums1)):
                prod = nums1[j] * nums1[k]
                if prod in d2:
                    count += d2[prod]

        return count
