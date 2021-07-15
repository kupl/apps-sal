class Solution:
    def maxDistance(self, arr: List[int], m: int) -> int:
        
        
        arr = sorted(arr)
        low, high = 1, arr[-1]-arr[0]+1
        
        def isValid(k, balls):
            balls-=1
            prev = arr[0]
            res = float('inf')
            for i in range(1,len(arr)):
                if arr[i]-prev >= k:
                    res = min(res, arr[i]-prev)
                    balls-=1
                    prev = arr[i]
                
                if balls == 0: break
                    
            return res if balls == 0 else -1
        
        ans = 0
        
        while low < high:
            mid = low + (high-low)//2
            tmp = isValid(mid, m)
            
            if tmp != -1:
                ans = tmp
                low = mid+1
            else:
                high = mid
        
        return ans
            
            
            
            
            

