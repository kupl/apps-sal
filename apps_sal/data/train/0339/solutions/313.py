class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        d = {}
        drev = {}
        
        for i,x in enumerate(nums2):
            if x in drev:
                drev[x].add(i)
            else:
                drev[x] = {i}
                
        
        # print(d)
        
        
        for idx1,x in enumerate(nums1):
            i2 = x*x
            d = drev.copy()
            drev.clear()
            for idx,j in enumerate(nums2):
                d[j].remove(idx)
                if j in drev:drev[j].add(idx)
                else: drev[j] = {idx}
                
                if i2%j == 0:
                    k = i2//j
                    if k in d:
                        ans+=len(d[k])                                
                                
                                
                                
        d = {}
        drev = {}
        
        for i,x in enumerate(nums1):
            if x in drev:
                drev[x].add(i)
            else:
                drev[x] = {i}
                
        
        # print(d)
        
        
        for idx1,x in enumerate(nums2):
            i2 = x*x
            d = drev.copy()
            drev.clear()
            for idx,j in enumerate(nums1):
                d[j].remove(idx)
                if j in drev:drev[j].add(idx)
                else: drev[j] = {idx}
                
                if i2%j == 0:
                    k = i2//j
                    if k in d:
                        ans+=len(d[k])           
        
                                
                                
        return ans
                                
    
                    
                

