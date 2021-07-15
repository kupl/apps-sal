class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        products1 = collections.defaultdict(int)
        products2 = collections.defaultdict(int)
        
        result = 0
        
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                p = nums1[i]*nums1[j]
                products1[p] += 1
        
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                p = nums2[i]*nums2[j]
                products2[p] += 1
        
        for num in nums1:
            result += products2[num*num]
        
        for num in nums2:
            result += products1[num*num]
        
        return result

