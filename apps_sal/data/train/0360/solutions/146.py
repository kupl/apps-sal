class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)
        total = 0
        parts = 1
        while(low < high):
            total = 0
            parts = 1
            mid = int((low + high) / 2)
            for w in weights:
                if total + w <= mid:
                    total = total + w
                else:
                    total = w
                    parts += 1
            if parts > D:
                low = mid + 1
            else:
                high = mid
        return low
