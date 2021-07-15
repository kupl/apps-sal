class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # find smallest k that koko can finish in H hours
        left = 1 
        right = max(piles)
        
        def can(k):
            return sum((p-1)//k + 1 for p in piles) <= H
            
            
        while left < right:
            mid = (left + right) //2 # mid=left<right, left=right
            if can(mid):
                right = mid
            else:
                left = mid + 1

        return right

