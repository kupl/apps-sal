class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        mid = max(position) // 2
        gap = max(1,mid//2)
        
        t = 0
        best = 0
        
        while True:
            c = 1
            last = position[0]
            for i in range(1,len(position)):
                if position[i] - mid >= last:
                    c+=1
                    last = position[i]
                    
            
                    
            if c>=m:
                best = max(best,mid)
                mid = mid + gap
                
                
            else:
                mid = mid - gap
                
            gap = gap//2
            gap = max(1,gap)
            t+=1
            
            if t==50:
                break
                
        return (best)
                

