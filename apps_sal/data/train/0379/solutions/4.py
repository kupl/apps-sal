class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        t1 = [0 for _ in range(n+1)]
        t2 = [0 for _ in range(m+1)]
        i,j = 1,1
        
        while i<n+1 and j <m+1:
            if nums1[i-1]==nums2[j-1]:
                t1[i] = max(t1[i-1],t2[j-1]) + nums1[i-1]
                t2[j] = max(t1[i-1],t2[j-1]) + nums2[j-1]
                
                i+=1
                j+=1
            
            elif nums1[i-1] < nums2[j-1]:
                t1[i] = t1[i-1] + nums1[i-1]
                i+=1
            
            else:
                t2[j] = t2[j-1] + nums2[j-1]
                j+=1
        
        while i<n+1:
            t1[i] = t1[i-1] + nums1[i-1]
            i+=1
        
        while j<m+1:
            t2[j] = t2[j-1] + nums2[j-1]
            j+=1
        
        
        return max(t1[-1],t2[-1]) % (10**9 + 7)         
