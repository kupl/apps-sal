class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isFeasible(mid, arr, n, k): 
            pos = arr[0] 
            elements = 1
  
            for i in range(1, n): 
                if arr[i] - pos >= mid: 
                    pos = arr[i] 
                    elements += 1
  
                    if elements == k: 
                        return True
            return False
        
        position = sorted(position)
        if m == 2:
            return position[-1] - position[0]    
        dist = []
        for i in range(len(position) -1):
            dist.append(position[i+1] - position[i])
        if m == len(position):
            return min(dist)
        
        left = 0
        right = position[-1]
        res = 1
        
        while left < right: 
            mid = (left + right) // 2
         
            if isFeasible(mid, position, len(position), m): 
                res = max(res, mid) 
                left = mid + 1
            else: 
                right = mid 
  
        return res 
        
            
            
            
        

