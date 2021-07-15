class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # time O(nlogw); space O(1)
        def possible(k):
            return sum((num-1) // k + 1 for num in piles) <= H
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if not possible(mid):
                left = mid + 1
            else:
                right = mid
        
        return left 
