class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def time_need(K):
            return sum(p//K + (1 if p%K else 0) for p in piles)
        
        low = max(1, sum(piles)//H)
        high = max(piles)
        while low < high:
            if time_need(low)<=H: return low
            
            low += 1
            mid = (low+high)//2
            if time_need(mid) > H:
                low = mid + 1
            else:
                high = mid
        
        return low
