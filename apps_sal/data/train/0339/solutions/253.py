class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        ans = 0
        for j in range(len(nums2)):
            for k in range(j+1, len(nums2)):
                if math.sqrt(nums2[j]*nums2[k]) in c1:
                    ans += c1[math.sqrt(nums2[j]*nums2[k])]
        
        for j in range(len(nums1)):
            for k in range(j+1, len(nums1)):
                if math.sqrt(nums1[j]*nums1[k]) in c2:
                    ans += c2[math.sqrt(nums1[j]*nums1[k])]
        
        return ans
    
                
            

