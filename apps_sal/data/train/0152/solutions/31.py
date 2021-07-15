class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        
        def is_valid(guess):
            prev = position[0]
            balls = 1
            for p in position[1:]:
                if p-prev >= guess:
                    prev = p
                    balls += 1
                if balls == m:  
                    return True
            return False
                    
        l, r = 1, (position[-1]-position[0]) // (m-1)
        while l < r:
            guess = (l + r + 1) >> 1 
            if is_valid(guess):
                l = guess
            else:    
                r = guess-1
        return l        
        


    #    position.sort()
    #    l, r = 1, position[-1] - position[0]
    #    while l < r:
    #        cand = (l + r + 1) >> 1
    #        if self.is_valid(position, m, cand):
    #            l = cand
    #        else:    
    #            r = cand - 1
    #    return l        
    #
    #def is_valid(self, position, m, cand):
    #    prev = position[0]
    #    rem = m - 1
    #    for pos in position[1:]: 
    #        if pos >= prev + cand:
    #            prev = pos
    #            rem -= 1
    #        if rem == 0:    
    #            return True
    #    return False

