class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        total = 0
        nums1Sum = {}
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                nums1Sum[nums1[i] * nums1[j]] = nums1Sum.get(nums1[i] * nums1[j], 0) + 1
        nums2Sum = {}
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                nums2Sum[nums2[i] * nums2[j]] = nums2Sum.get(nums2[i] * nums2[j], 0) + 1
        for num in nums1:
            if num * num in nums2Sum:
                total += nums2Sum[num * num]
        for num in nums2:
            if num * num in nums1Sum:
                total += nums1Sum[num * num]
        return total
