class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1_e = Counter()
        cnt1_ne = Counter()
        
        for i in range(len(nums1)):
            cnt1_e[nums1[i]**2] += 1
            for j in range(i+1, len(nums1)):
                cnt1_ne[nums1[i]*nums1[j]] += 1
            
        cnt2_e = Counter()
        cnt2_ne = Counter()
        
        for i in range(len(nums2)):
            cnt2_e[nums2[i]**2] += 1
            for j in range(i+1, len(nums2)):
                cnt2_ne[nums2[i]*nums2[j]] += 1  
        res = 0
        for k1, v1 in list(cnt1_e.items()):
            if k1 in list(cnt2_ne.keys()):
                res += v1 * cnt2_ne[k1]
       
        for k2, v2 in list(cnt2_e.items()):
            if k2 in list(cnt1_ne.keys()):
                res += v2 * cnt1_ne[k2]
         
        return res
                    
            
            

