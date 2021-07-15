class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        arr = arr[::-1]
        v = arr.pop()
        cnt = 0
        while arr:     
            while arr and v > arr[-1]: 
                cnt += 1
                arr.pop()
                if cnt >= k: 
                    return v
            if not arr: 
                return v
            v = arr.pop() 
            cnt = 1 # already won the previous comparison
            if cnt >= k: 
                return v
            
        return v
            
            
                
        
                
                
                
            

