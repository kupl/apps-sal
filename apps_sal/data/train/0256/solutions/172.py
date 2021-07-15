class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low, high = 1, max(piles)
        
        def isPossible(eatRate):
            total = 0
            for numBanana in piles:
                total += ((numBanana-1)//eatRate) + 1
            return total <= H
        
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1
                
        return low
