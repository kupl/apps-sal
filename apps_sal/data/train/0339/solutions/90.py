class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        squares1 = Counter()
        squares2 = Counter()
        for num in nums1:
            squares1[num*num] += 1
        for num in nums2:
            squares2[num*num] += 1
        
        numTriplets = 0
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in squares2:
                    numTriplets += squares2[nums1[i] * nums1[j]]
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in squares1:
                    numTriplets += squares1[nums2[i] * nums2[j]]
        return numTriplets
