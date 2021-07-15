class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()        
        w = (position[-1] - position[0]) // (m-1)
        
        def count(w, m):
            idx = 0
            m -= 1
            for i in range(1, len(position)):
                if position[i] - position[idx] >= w:
                    idx = i
                    m -= 1
                
                if m == 0:
                    break
                    
            return m == 0


        if count(w, m):
            return w
        else:    
            l ,r = 0, w
            while l < r:
                mid = r - (r - l) // 2
                if count(mid, m):
                    l = mid
                else:
                    r = mid - 1
                
            return l
            
            

