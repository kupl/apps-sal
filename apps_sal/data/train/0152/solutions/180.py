class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def guess(position, m, guess):
            placed = 1
            last = position[0]
            i = 1
            while i < len(position):
                #print(position[i], last, placed, m)
                if position[i] - last >= guess:
                    placed += 1
                    last = position[i]
                
                if placed == m:
                    return True
                
                i += 1
            
           # print(\"final \", placed, m)
            return placed >= m
        
        position.sort()
        l = 0
        r = position[-1] - position[0]
        # l: checked OK
        # r: haven't check
        while l < r:
            mid = (l + r + 1) // 2
            #print(l, mid, r)
            if guess(position, m, mid):
                #print(\"guess OK\", mid)
                l = mid
            else:
                r = mid - 1
        
        return l
    
    
    #placed = 1, last = 1, i = 1
    # 
        

