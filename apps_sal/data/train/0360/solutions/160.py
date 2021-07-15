class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right)//2
            current = 0
            need = 1
            for w in weights:
                if current + w > mid:
                    need += 1
                    current = 0
                current += w
                
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left

