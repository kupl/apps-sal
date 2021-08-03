class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        sums = {}
        sums2 = {}
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in sums:
                    sums[nums2[i] * nums2[j]] += 1
                else:
                    sums[nums2[i] * nums2[j]] = 1
        for i in nums1:
            if i**2 in sums:
                result += sums[i**2]
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in sums2:
                    sums2[nums1[i] * nums1[j]] += 1
                else:
                    sums2[nums1[i] * nums1[j]] = 1
        for i in nums2:
            if i**2 in sums2:
                result += sums2[i**2]
        return result
