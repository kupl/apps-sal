class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n, l = len(arr), 0 
        
        while l+1 < n and arr[l+1] >= arr[l]: 
            l += 1  
            
        if l == n-1: 
            return 0   
        
        r = n-1
        
        while r > 0 and arr[r-1] <= arr[r]: 
            r -= 1          
            
        if arr[l] <= arr[r]: 
            return r-l-1
        
        ans = min(n-l-1, r)
        
        for i in range(l+1): 
            if arr[i] <= arr[r]: 
                ans = min(ans, r-i-1)               
            elif r < n-1: 
                r += 1

        return ans
