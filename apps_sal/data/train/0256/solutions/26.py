class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def condition(k) -> bool:
            count = 0
            
            for v in piles:
                count += int(math.ceil(v / k))
                if count > H:
                    return False
            return True
        
        left,right = 1,max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
