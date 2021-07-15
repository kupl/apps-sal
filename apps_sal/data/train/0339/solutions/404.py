class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dict1 = Counter([x**2 for x in nums1])
        dict2 = Counter([x**2 for x in nums2])
        
        count=0
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                count += dict1[nums2[i]*nums2[j]]
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                count += dict2[nums1[i]*nums1[j]]
        
        return count
