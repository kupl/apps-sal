class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
               
        res = 0
        cnt1 = collections.Counter()
        for j in range(len(nums2)):
            for i in range(len(nums1)):
                s = nums1[i]**2
                if s%nums2[j] == 0 and s//nums2[j] in cnt1:
                    res += cnt1[s//nums2[j]]    
                
            cnt1[nums2[j]] +=1
                    
        cnt2 = collections.Counter()
        for j in range(len(nums1)):
            for i in range(len(nums2)):
                s = nums2[i]**2
                if s%nums1[j] == 0 and s//nums1[j]  in cnt2:
                    res += cnt2[ s//nums1[j] ]    
                
            cnt2[nums1[j]] +=1 
                    
        return res
        
                    
        

