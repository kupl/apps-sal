from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def doesViolate(mid):
            requiredHour = 0
            for i in range(0, len(piles)):
                if mid > piles[i]:
                    requiredHour+=1
                else:
                    requiredHour += math.ceil(piles[i]/mid)
            if requiredHour > H:
                return True
            else: return False
        low = 1
        high = max(piles)
        
        while (low < high):
            mid = (low+high) // 2
            if doesViolate(mid) == True:
                low = mid + 1
            else:
                high = mid
        return low

