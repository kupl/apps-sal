class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Minimum value we can have is the sum of piles / H
        lo = sum(piles) // H
        
        # Maximum would be the maximum value in the list
        hi = max(piles)
        
        #
        #         lo = 0
        #         hi = float('-inf')

        #         for pile in piles:
        #             lo += pile
        #             hi = max(hi, pile)

        #         lo =// H
        
        if len(piles) == 1:
            return ceil(piles[0] / H)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            count = sum(map(lambda x: ceil(x / mid), piles))
            
            if count > H:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
