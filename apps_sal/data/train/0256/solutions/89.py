import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        '''
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
        '''
        
        
        # solution: use binary guess
        
        
        le = 1
        ri = sum(piles)
        
        def checkHours(speed):
            s = 0
            for item in piles:
                s+=math.ceil(item/speed)
            return s
            '''
            sum_hours = 0
            for i in piles:
                bananas =  i
                hours = 0
                while True:
                    bananas = bananas - speed
                    hours += 1
                    if bananas <= 0: # bug only <
                        break
                sum_hours += hours
            return sum_hours
            '''
                        
        
        while le + 1 < ri:
            mid = le + (ri - le)//2
            result = checkHours(mid)
            if result <= H : # decrease speed
                ri = mid
            else: # increase speed
                le =  mid
                
        result = checkHours(le)
 
        if result <= H: # changed to <= H
            return le
        else:
            return ri


