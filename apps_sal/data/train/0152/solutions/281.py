class Solution:
    def maxDistance(self, arr: List[int], m: int) -> int:
        arr.sort()
        
        def isFeasible(mid): 
            pos = arr[0] 

            # Initialize count of elements placed. 
            elements = 1

            # Try placing k elements with minimum 
            # distance mid. 
            for i in range(1, len(arr)): 
                if (arr[i] - pos >= mid): 

                    # Place next element if its distance  
                    # from the previously placed element 
                    # is greater than current mid 
                    pos = arr[i] 
                    elements += 1

                    # Return if all elements are placed 
                    # successfully 
                    if (elements == m): 
                        return True
            return 0
  
        
        hi = arr[-1] - arr[0]
        lo = float('inf')
        for i in range(len(arr)-1):
            lo = min(lo, arr[i+1]-arr[i])
        
        ans = float('-inf')
        
        while lo<=hi:
            mid = (lo+hi)//2
            if isFeasible(mid):
                ans = max(ans, mid)
                lo = mid+1
            else:
                hi = mid-1
        
        return ans
    
    
    
                
   
        
        
        

