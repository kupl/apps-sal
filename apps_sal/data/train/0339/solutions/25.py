from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        squares1 = Counter([x**2 for x in nums1])
        squares2 = Counter([x**2 for x in nums2])
        
        count = 0
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i]*nums1[j] in squares2:
                    count = count + squares2[nums1[i]*nums1[j]]
        
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i]*nums2[j] in squares1:
                    count = count + squares1[nums2[i]*nums2[j]]
                    
        return count
        

