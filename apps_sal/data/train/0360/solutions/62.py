class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(w) -> bool:
            curr,k = 0,0
            count = 0
            while k < len(weights):
                if curr + weights[k] > w:
                    count += 1
                    if count > D:
                        return False
                    curr = 0
                curr += weights[k]
                k += 1
            
            return count + 1 <= D
        
        left,right = max(weights),sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
