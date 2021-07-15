class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        d1 = {}
        d2 = {}
        
        t1 = {}
        t2 = {}
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        
        for i in range(l1):
            d1[nums1[i]] = i
            
        for i in range(l2):
            d2[nums2[i]] = i
            
            
        def runList1(i):
            
            if i == l1:
                return 0           
            
            if i in t1:
                return t1[i]
            
            maxList2 = 0
                        
            if i + 1 < l1 and  nums1[i+1] in d2:
                maxList2 = runList2(d2[nums1[i+1]])
                
            result = max(runList1(i+1), maxList2) + nums1[i]
            t1[i] = result
            return result
        
        
        def runList2(i):
            if i == l2:
                return 0
            
            if i in t2:
                return t2[i]
            
            maxList1 = 0
                       
            
            if i+1 < l2 and nums2[i+1] in d1:
                maxList1 = runList1(d1[nums2[i+1]])
                            
            result = max(runList2(i+1), maxList1) + nums2[i]
            
            t2[i] = result
            
            
            return result
             
        value = max(runList1(0), runList2(0)) 
        
        return value % (10**9 + 7)
        
        

