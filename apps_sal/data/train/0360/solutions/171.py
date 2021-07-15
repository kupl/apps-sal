from collections import defaultdict
class Solution:
     def canShipWithinDays(self, weights: List[int], D: int, maxWeight: int) -> bool:
        if max(weights) > maxWeight:
            return False
        
        lswt = 0
        nD = 1
        for w in weights:
            if lswt + w <= maxWeight:
                lswt += w
            else:
                nD += 1
                lswt = w
        return nD <= D
    
     def shipWithinDays(self, weights: List[int], D: int) -> int:
        maxweight = sum(weights)
        minweight = max(weights)
        while maxweight > minweight + 1:
            mw = (maxweight + minweight) // 2 
            if self.canShipWithinDays(weights, D, mw):
                maxweight = mw
            else:
                minweight = mw
        
        if self.canShipWithinDays(weights, D, minweight):
            return minweight
        else:
            return maxweight
