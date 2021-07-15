class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def possible_with_capacity(c):
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > c:
                    total = weight
                    days += 1
                    if days > D:
                        return False
            return True
        
        while left < right:
            cap = left + (right-left)//2
            if possible_with_capacity(cap):
                right = cap
            else:
                left = cap + 1
        
        return left
